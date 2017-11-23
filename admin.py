from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from django.contrib.admin.sites import AlreadyRegistered
from django import forms
from django.http import HttpResponse

from redactor.widgets import RedactorEditor

from .models import Article, Tag, Category, Content, Media, Page

from hvad.admin import TranslatableAdmin
from hvad.forms import TranslatableModelForm

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class CamomillaUserAdmin(UserAdmin):
    fieldsets = ()
    exclude = ('groups',)
    readonly_fields = ('last_login', 'date_joined',)

    def get_queryset(self, request):
        qs = super(CamomillaUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)

    def get_form(self, request, obj=None, **kwargs):
        current_user = request.user
        if not current_user.is_superuser:
            self.exclude = (
                'groups', 'is_superuser', 'user_permissions',
                'is_staff', 'is_active', 'level'
            )
        form = super(CamomillaUserAdmin, self).get_form(request, obj, **kwargs)
        form.current_user = current_user
        return form


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdminForm(TranslatableModelForm):
    class Meta:
        model = Article
        exclude = ('slug',)
        widgets = {
           'content': RedactorEditor(),
        }


class ArticleAdmin(TranslatableAdmin):
    filter_horizontal = ('tags', 'categories')
    form = ArticleAdminForm


class TagAdmin(TranslatableAdmin):
    exclude = ('slug',)
    readonly_fields = ('get_slug',)


class CategoryAdmin(TranslatableAdmin):
    pass


class ContentAdminForm(TranslatableModelForm):
    class Meta:
        model = Content
        exclude = ('author',)
        widgets = {
           'content': RedactorEditor(),
        }


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


class SitemapUrlAdmin(TranslatableAdmin):
    pass

class PageAdmin(TranslatableAdmin):
    pass

try:
    admin.site.register(get_user_model(), CamomillaUserAdmin)
except AlreadyRegistered:
    raise Exception ('You need to define your own AUTH_USER_MODEL. Please follow the README.md')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Page, PageAdmin)
admin.site.unregister(Group)

admin.site.index_title = '{0} {1}'.format(
    _('Administration panel for'),
    getattr(settings, 'PROJECT_TITLE', 'Camomilla')
)
