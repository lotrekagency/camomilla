from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from camomilla.settings import PROJECT_TITLE
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from modeltranslation.forms import TranslationModelForm

from camomilla.models import Article, Content, Media, MediaFolder, Page, Tag


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdminForm(TranslationModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        exclude = ("slug",)


class ArticleAdmin(TranslationAdmin):
    filter_horizontal = ("tags",)
    form = ArticleAdminForm


class TagAdmin(TranslationAdmin):
    pass


class MediaFolderAdmin(admin.ModelAdmin):
    pass


class ContentAdminForm(TranslationModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = "__all__"


class ContentAdmin(TranslationAdmin):
    form = ContentAdminForm


class MediaAdmin(TranslationAdmin):
    exclude = (
        "thumbnail",
        "size",
        "image_props",
    )
    readonly_fields = ("image_preview", "image_thumb_preview")
    list_display = (
        "__str__",
        "title_tag",
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


class PageAdmin(TranslationAdmin):
    exclude = ("permalink",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(MediaFolder, MediaFolderAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Page, PageAdmin)

admin.site.index_title = "{0} {1}".format(_("Administration panel for"), PROJECT_TITLE)
