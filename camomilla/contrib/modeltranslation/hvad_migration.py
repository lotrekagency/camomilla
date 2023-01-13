from django.conf import settings
from django.db import migrations, connection


class KeepTranslationsMixin:

    _saved_data_from_plain = {}
    language_codes = dict(getattr(settings, "LANGUAGES", {})).keys()

    def is_operation_legit(self, o):
        return not (
            isinstance(o, migrations.RemoveField)
            and o.name == "master"
            and o.model_name.endswith("translation")
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operations = [o for o in self.operations if self.is_operation_legit(o)]
        self.operations.insert(
            0, migrations.RunPython(self._getDataFromHvad, self._restoreDataToHvad)
        )
        self.operations.append(
            migrations.RunPython(
                self._restoreDataToModelTranslation, self._getDataFromModelTranslation
            )
        )

    def _getDataFromHvad(self, apps, schemaeditor):
        for modelPath, fields in self.keep_translations.items():
            Model = apps.get_model(*modelPath.split("."))
            table = Model._meta.db_table + "_translation"
            if not "language_code" in fields:
                fields = ("language_code",) + fields
            with connection.cursor() as cursor:
                cursor.execute("SELECT master_id FROM {0};".format(table))
                masters = list(set(cursor.fetchall()))
                for master in masters:
                    cursor.execute(
                        "SELECT {0} FROM {1} WHERE master_id={2};".format(
                            ",".join(fields), table, master[0]
                        )
                    )
                    rows = cursor.fetchall()
                    self._saved_data_from_plain[
                        modelPath
                    ] = self._saved_data_from_plain.get(modelPath, {})
                    self._saved_data_from_plain[modelPath][
                        master[0]
                    ] = self._saved_data_from_plain[modelPath].get(master[0], [])
                    for row in rows:
                        self._saved_data_from_plain[modelPath][master[0]].append(
                            dict(zip(fields, row))
                        )

    def _getDataFromModelTranslation(self, apps, schemaeditor):
        pass
        # for modelPath, fields in self.keep_translations.items():
        #     Model = apps.get_model(*modelPath.split('.'))
        #     table = Model._meta.db_table
        #     trans_fields = ('id',)
        #     for language_code in self.language_codes:
        #         trans_fields += ("{0}_{1}".format(field, language_code) for field in fields if field != "id")
        #     with connection.cursor() as cursor:
        #         cursor.execute("SELECT {0} FROM {1}".format(','.join(trans_fields), table))
        #         rows = cursor.fetchall()
        #         self._saved_data_from_plain[modelPath] = []
        #         for row in rows:
        #             self._saved_data_from_plain[modelPath].append(dict(zip(fields, row)))

    def _restoreDataToModelTranslation(self, apps, schemaeditor):
        for key, master_dict in self._saved_data_from_plain.items():
            Model = apps.get_model(*key.split("."))
            for pk, translations in master_dict.items():
                obj = Model.objects.get(pk=pk)
                for translation in translations:
                    lang = translation.pop("language_code")
                    for attr, value in translation.items():
                        setattr(obj, "{0}_{1}".format(attr, lang), value)
                obj.save()

    def _restoreDataToHvad(self, apps, schemaeditor):
        pass
        # for key, rows in self._saved_data_from_plain.items():
        #     Model = apps.get_model(*key.split('.'))
        #     key = key + 'Translation'
        #     ModelTanslatable = apps.get_model(*key.split('.'))
        #     for row in rows:
        #         obj_to_trans = Model.objects.get(pk=row['id'])
        #         for language_code in self.language_codes:
        #             obj, _ = ModelTanslatable.objects.get_or_create(
        #                 master=obj_to_trans, language_code=language_code
        #             )
        #             for attribute, attribute_value in row.items():
        #                 if attribute != 'id' and attribute.endswith(language_code):
        #                     setattr(obj, attribute.rstrip('_{0}'.format(language_code)), attribute_value)
        #             obj.save()
