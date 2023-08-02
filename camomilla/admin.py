from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from camomilla import settings

if settings.ENABLE_TRANSLATIONS:
    from modeltranslation.admin import TabbedTranslationAdmin as TranslationAwareModel
else:
    from django.contrib.admin import ModelAdmin as TranslationAwareModel

from camomilla.models import Article, Content, Media, MediaFolder, Page, Tag


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ("slug",)
        widgets = {"content": CKEditorUploadingWidget}


class ArticleAdmin(TranslationAwareModel):
    filter_horizontal = ("tags",)
    form = ArticleAdminForm


class TagAdmin(TranslationAwareModel):
    pass


class MediaFolderAdmin(admin.ModelAdmin):
    readonly_fields = ("path",)


class ContentAdminForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"
        widgets = {"content": CKEditorUploadingWidget}


class ContentAdmin(TranslationAwareModel):
    form = ContentAdminForm


class MediaAdmin(TranslationAwareModel):
    exclude = (
        "thumbnail",
        "size",
        "image_props",
    )
    readonly_fields = ("image_preview", "image_thumb_preview", "mime_type")
    list_display = (
        "__str__",
        "title",
        "image_thumb_preview",
    )

    def response_add(self, request, obj):
        if request.GET.get("_popup", ""):
            return HttpResponse(
                """
               <script type="text/javascript">
                  opener.dismissAddRelatedObjectPopup(window, %s, '%s');
               </script>"""
                % (obj.id, obj.json_repr)
            )
        else:
            return super(MediaAdmin, self).response_add(request, obj)


class PageAdmin(TranslationAwareModel):
    exclude = ("permalink",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(MediaFolder, MediaFolderAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Page, PageAdmin)

