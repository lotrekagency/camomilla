from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin.sites import AlreadyRegistered
from django import forms
from django.http import HttpResponse

from .models import Article, Tag, Category, Content, Media, Page, MediaFolder
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from hvad.admin import TranslatableAdmin
from hvad.forms import TranslatableModelForm

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdminForm(TranslatableModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        exclude = ('slug',)


class ArticleAdmin(TranslatableAdmin):
    filter_horizontal = ('tags', 'categories')
    form = ArticleAdminForm


class TagAdmin(TranslatableAdmin):
    pass


class CategoryAdmin(TranslatableAdmin):
    pass

class MediaFolderAdmin(TranslatableAdmin):
    pass

class ContentAdminForm(TranslatableModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Content


class ContentAdmin(TranslatableAdmin):
    form = ContentAdminForm


class MediaAdmin(TranslatableAdmin):
    exclude = ('thumbnail', 'size', 'is_image')
    readonly_fields = ('image_preview', 'image_thumb_preview')
    list_display = ('__str__', 'name', 'image_thumb_preview',)

    def response_add(self, request, obj):
        if request.GET.get('_popup', ''):
            return HttpResponse('''
               <script type="text/javascript">
                  opener.dismissAddRelatedObjectPopup(window, %s, '%s');
               </script>''' % (obj.id, obj.json_repr)
            )
        else:
            return super(MediaAdmin, self).response_add(request, obj)


class PageAdmin(TranslatableAdmin):
    pass
    # def __init__(self, *args, **kwargs):
    #     super(PageAdmin, self).__init__(*args, **kwargs)
    #     self.fieldsets = (
    #         ('SEO', {
    #             'fields': (
    #                 'title', 'description', 'permalink',
    #                 'og_image', 'og_description',
    #                 'og_title', 'og_type', 'og_url',
    #                 'canonical',
    #             ),
    #         }),
    #     )


class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MediaFolder, MediaFolderAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Page, PageAdmin)

admin.site.index_title = '{0} {1}'.format(
    _('Administration panel for'),
    getattr(settings, 'PROJECT_TITLE', 'Camomilla')
)
