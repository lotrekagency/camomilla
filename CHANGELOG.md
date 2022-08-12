# Changelog

<!--next-version-placeholder-->

## v5.7.5 (2022-08-11)
### Fix
* Explicit default_auto_field in app config to prevent unwanted migrations ([`ec33de8`](https://github.com/lotrekagency/camomilla/commit/ec33de87be8f7fc7fc466070e8fe20b7e75ef438))

## v5.7.4 (2022-08-02)
### Fix
* Added missing migrations ([`e57989e`](https://github.com/lotrekagency/camomilla/commit/e57989e7174374bdcff19d042956327e12b65fe4))
* Fix media migration to be compliant with hvad ([`dc5e83a`](https://github.com/lotrekagency/camomilla/commit/dc5e83ad0d639024319a49ac00b01f8845fbe9f1))
* Fix makefile ([`925a270`](https://github.com/lotrekagency/camomilla/commit/925a2706f00c2b6ab5cc9055a557192a4bbd8d4a))
* Added missing migrations for django 4 ([`8a79998`](https://github.com/lotrekagency/camomilla/commit/8a79998e39c9555385ab0d9e87f299b0ede2883d))

## v5.7.3 (2022-05-16)
### Fix
* Fix Arrayfield import ([`2cfdaca`](https://github.com/lotrekagency/camomilla/commit/2cfdacacb63d59cea79ae59f0c3d9839efe56088))
* Fix jsonfield imports ([`be4b566`](https://github.com/lotrekagency/camomilla/commit/be4b56622df269ee5d200dc5666536b39e7fe0cc))

## v5.7.2 (2022-05-13)
### Fix
* Fix get page to work with new hvad ([`2cd8b89`](https://github.com/lotrekagency/camomilla/commit/2cd8b8948df44fd82c214835770e92b10a3f5512))
* Fix camomilla filter content to work with new hvad ([`0193509`](https://github.com/lotrekagency/camomilla/commit/019350929c19cccdfedbdfc2b493039484a08400))
* Update camomilla template to support new django admin static ([`92afbc0`](https://github.com/lotrekagency/camomilla/commit/92afbc07a1345cf19ed4a5a83317f7658b008804))
* Fix gettext_lazy import deprecated in django4 ([`626dfe1`](https://github.com/lotrekagency/camomilla/commit/626dfe16a9fb6457e463ac995eb9d4d809c51e22))

## v5.7.1 (2022-03-30)
### Fix
* Fix circular import error ([`8b3f6ff`](https://github.com/lotrekagency/camomilla/commit/8b3f6ff2d7a01a2f138506ef4ad94fe78b691521))
* Fix session login urls ([`2688c1a`](https://github.com/lotrekagency/camomilla/commit/2688c1aae082654bebd84f3bfd8f2b74104fa930))
* Fix drf session authentication ([`538e709`](https://github.com/lotrekagency/camomilla/commit/538e709dcc8fd2799b4063c265687b2e0315c076))

## v5.7.0 (2022-03-14)
### Feature
* Added ordering to Articles Categories and Pages ([`8cb6d75`](https://github.com/lotrekagency/camomilla/commit/8cb6d752e462462c37add877c056827fddb491cc))
* Added meta to Articles Categories and Pages ([`f859c37`](https://github.com/lotrekagency/camomilla/commit/f859c370add3b34c081edccc4925c0cd99064d42))
* Meta mixin for models 🦹 ([`88c4b4a`](https://github.com/lotrekagency/camomilla/commit/88c4b4afbfc042ea024c9f4ab6090ccb5b73b272))
* Added ordering mixin for rest framework inspired by django adminsortable2 ([`cb619bc`](https://github.com/lotrekagency/camomilla/commit/cb619bcb10650174d8e01835fdb9ecf44ece81a7))

### Fix
* Fix meta mixin methods ([`7d7e3a8`](https://github.com/lotrekagency/camomilla/commit/7d7e3a80bda93a5faec92ebe52ed7be28635790d))
* Fixed reverse ordering in update_order endpoint ([`b8ae096`](https://github.com/lotrekagency/camomilla/commit/b8ae0962bdb75895945b0cc696fb64647e079b31))
* Fix pagination ordering without default order field ([`ca07303`](https://github.com/lotrekagency/camomilla/commit/ca07303c951fe4e6142a8af74ff282d0f90c67c2))

## v5.6.1 (2022-03-01)
### Fix
* Fix pagination mixin to provide order filter and search also for unpaginated queries ([`62e8b01`](https://github.com/lotrekagency/camomilla/commit/62e8b01433aac97a5b70de6197f7bb957e5abf46))

## v5.6.0 (2022-02-26)
### Feature
* Added permission classes to media api ([`558cac2`](https://github.com/lotrekagency/camomilla/commit/558cac2a2b852dcd76d2ad20ce1ab14b4ccb01b0))
* Auto-order pagination mixins ([`125dd71`](https://github.com/lotrekagency/camomilla/commit/125dd71b05faa6554a9def76bd664b837ca8d8fe))
* **serializers:** Automagically 🧙 create nested serializers at runtime avoiding the need of declaring RelatedField classes ([`4748786`](https://github.com/lotrekagency/camomilla/commit/47487860494b56f5fdbff11b4bcc1790e2f9581a))

### Fix
* Fix paginate stack oredering ([`685cf8d`](https://github.com/lotrekagency/camomilla/commit/685cf8dbca2aae00fd2536ed1e1dca6696e88734))

## v5.5.2 (2022-02-14)
### Fix
* Fix djsuperadmin reverse url ([`035d377`](https://github.com/lotrekagency/camomilla/commit/035d377ef9c4dfc25516103542c0aea28a0445a6))

## v5.5.1 (2022-02-14)
### Fix
* Fix RelatedField allow_insert condition ([`90ba04f`](https://github.com/lotrekagency/camomilla/commit/90ba04f2520bf131c95145121362984535f367e2))
* Fix serarchfield for article viewset ([`2c9cda4`](https://github.com/lotrekagency/camomilla/commit/2c9cda4f387bc4bbc5909f7f40ebd484591cb402))
* Added missing migration ([`a018f0f`](https://github.com/lotrekagency/camomilla/commit/a018f0f125e68548492d3fd74a5cd8bddda61293))
* Refactor filefield and fix bad return value ([`1f1a36a`](https://github.com/lotrekagency/camomilla/commit/1f1a36aaa2fad7e43a348ef2513e1aaabdddaae3))
* Fix related field trying to insert new values all the time ([`2465598`](https://github.com/lotrekagency/camomilla/commit/246559814ef351d2cd010fd6f7385777dd075cf2))

## v5.5.0 (2022-02-12)
### Feature
* **api:** Brand new serializators views and permissions for users endpoint ([`0f5b824`](https://github.com/lotrekagency/camomilla/commit/0f5b824c0c614d9ec8fbb1ffd04644e3d30e774c))
* **api:** Added trigram search mixin to medias ([`0002c8b`](https://github.com/lotrekagency/camomilla/commit/0002c8b40a317b3d6bae64c1c12764e31e59cb6c))

### Fix
* Fix File fields imports ([`3a0af76`](https://github.com/lotrekagency/camomilla/commit/3a0af764afefc88336bcb0646e13dc3c9deee609))
* Added creation logics for Related fields ([`56f20a5`](https://github.com/lotrekagency/camomilla/commit/56f20a5df522035ef5bbdca6e8c67bfa40daf274))
* Integrate Camomilla fields in Base model serializers ([`3556d33`](https://github.com/lotrekagency/camomilla/commit/3556d33c7343208b9f7b0e380bb1614c24298169))
* Added FileField and ImageField to fix drf Fields ([`7fc3160`](https://github.com/lotrekagency/camomilla/commit/7fc3160b493cc102ffa1be029e651bc3196266cc))
* Article permalink is now slugfield to prevent bad inputs ([`aafd92c`](https://github.com/lotrekagency/camomilla/commit/aafd92cb518fe5e768ad3fd6f515af0c8599747a))
* Fix article serializer missing categories ([`93b4284`](https://github.com/lotrekagency/camomilla/commit/93b42840980da194dd6b40646d7d5685c7da930a))

## v5.4.2 (2022-01-18)
### Fix
* Fix versioning ([`39b5226`](https://github.com/lotrekagency/camomilla/commit/39b522637ff79c7ff05237d1ad85e1cae26d2a94))
* Added min max range to requirements ([`6841054`](https://github.com/lotrekagency/camomilla/commit/6841054d71c0704919b446eb8ed542d3fb08a873))

## v5.4.1 (2022-01-17)
### Fix
* Loosen the range of requirements package versions ([`96d491b`](https://github.com/lotrekagency/camomilla/commit/96d491b4ff0aba269624eb7a27b1f3cd55946721))

## v5.4.0 (2022-01-13)
### Feature
* **media:** Added mime_type column to media model ([`4771068`](https://github.com/lotrekagency/camomilla/commit/4771068d2e54779a3d6e38ee9b447fb04c73539c))
* **api:** Added search to medias ([`905661d`](https://github.com/lotrekagency/camomilla/commit/905661d874b5ff2e22ea8b508c46d1ccfc70c0e7))
* **media:** Added option to override Media file on update from api to maintain same url ([`8d6371f`](https://github.com/lotrekagency/camomilla/commit/8d6371ff94e460f2e84efde45882d7d192b7cce6))

### Fix
* **media:** Added opetation to db  migration to recalc old media with the new mime_type feature ([`a7afd2d`](https://github.com/lotrekagency/camomilla/commit/a7afd2d53ba2b2f27d0d06fb6dba131368fdcc6e))
* **media:** Mime filter parsing works also in folder viewset ([`4149e92`](https://github.com/lotrekagency/camomilla/commit/4149e92e6c67e5f96219f02859a3aaa3f748553d))

## v5.3.0 (2021-12-17)
### Feature
* **api:** Handle multisort on PaginateStackMixin ([`40080f4`](https://github.com/lotrekagency/camomilla/commit/40080f4542c8e0dd4c8b36bb5cf5de6e078c3314))

## v5.2.0 (2021-12-17)


## v5.1.0 (2021-12-17)
### Feature
* Added image properties into media model ([`09cb481`](https://github.com/lotrekagency/camomilla/commit/09cb4818b2e3207eab7a12361f5e273b17edd1d0))
* Option to remove pagination on views ([`3e6fc48`](https://github.com/lotrekagency/camomilla/commit/3e6fc489db8b01f488ffebedd93f614c01d9e8d3))

### Fix
* Fix sqlite compatibility problems ([`4cde4fc`](https://github.com/lotrekagency/camomilla/commit/4cde4fc6c5f0e0b0d76e2020943de6d0bc973a49))
* Fix app name ([`13bb12d`](https://github.com/lotrekagency/camomilla/commit/13bb12d75bc9072a9ff150a7b408157f022c9299))
* Added search field to article viewset ([`1bd4b5f`](https://github.com/lotrekagency/camomilla/commit/1bd4b5f0681885b19bb2043d7622c8b3e77b9689))
* Fix articles and pages serializers requiring RelatedField fields. ([`c4fd330`](https://github.com/lotrekagency/camomilla/commit/c4fd330fb06dc3d49de4100865376a9eedb3f6f6))

## v5.0.3 (2021-10-26)


## v5.0.2 (2021-10-26)

