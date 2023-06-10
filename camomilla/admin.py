from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from camomilla.settings import PROJECT_TITLE
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from modeltranslation.settings import ENABLE_REGISTRATIONS
if ENABLE_REGISTRATIONS:
    from modeltranslation.admin import TranslationAdmin as TranslationAwareModel
    from modeltranslation.forms import TranslationModelForm as TranslationAwareModelForm
else:
    from django.contrib.admin import ModelAdmin as TranslationAwareModel
    from django.forms import ModelForm as TranslationAwareModelForm
    

from camomilla.models import Article, Content, Media, MediaFolder, Page, Tag


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdminForm(TranslationAwareModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        exclude = ("slug",)


class ArticleAdmin(TranslationAwareModel):
    filter_horizontal = ("tags",)
    form = ArticleAdminForm


class TagAdmin(TranslationAwareModel):
    pass


class MediaFolderAdmin(admin.ModelAdmin):
    pass


class ContentAdminForm(TranslationAwareModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = "__all__"


class ContentAdmin(TranslationAwareModel):
    form = ContentAdminForm


class MediaAdmin(TranslationAwareModel):
    exclude = (
        "thumbnail",
        "size",
        "image_props",
    )
    readonly_fields = ("image_preview", "image_thumb_preview")
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

admin.site.index_title = "{0} {1}".format(_("Administration panel for"), PROJECT_TITLE)
