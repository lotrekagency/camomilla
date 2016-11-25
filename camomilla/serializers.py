from rest_framework import serializers, permissions
from rest_framework.authtoken.models import Token

from .models import Article, Tag, Category, Content, Media, SitemapUrl, UserProfile

from hvad.contrib.restframework import TranslatableModelSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    user_permissions = PermissionSerializer(source='user.user_permissions', many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True, required=False, allow_null=True, allow_blank=True)
    repassword = serializers.CharField(write_only=True, required=False, allow_null=True, allow_blank=True)
    level = serializers.CharField(source="profile.level", required=False)
    has_token = serializers.SerializerMethodField('get_token', read_only=True)

    def get_token(self, obj):
        try:
            obj.auth_token
            return True
        except:
            return False

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'repassword', 'level', 'user_permissions', 'has_token')

    def validate(self, data):
        new_password = data.get('password', '')
        if new_password and len(new_password) < 8:
            raise serializers.ValidationError(_("Passwords too short"))
        if new_password != data.get('repassword', ''):
            raise serializers.ValidationError(_("Passwords should match"))
        return data

    def create(self, validated_data):
        user = get_user_model()(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        if validated_data.get('password', ''):
            user.set_password(validated_data['password'])
        user.save()
        profile = validated_data.get('profile', '')
        if profile:
            user.profile.level = profile['level']
        user.profile.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('password', ''):
            instance.set_password(validated_data['password'])
        profile = validated_data.get('profile', '')
        if profile:
            instance.profile.level = profile['level']
        instance.profile.save()
        permissions = validated_data.get('user_permissions', [])
        instance.user_permissions.clear()
        for permission in permissions:
            instance.user_permissions.add(permission)
        return instance


class TagSerializer(TranslatableModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(TranslatableModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class UnderTranslateMixin(object):

    def __init__(self, *args, **kwargs):
        self.ulanguage = 'en'
        try:
            self.ulanguage = kwargs.pop('ulanguage')
        except KeyError:
            pass
        super(UnderTranslateMixin, self).__init__(*args, **kwargs)


class ContentSerializer(TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class MediaSerializer(TranslatableModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'


#http://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers
class ArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ExpandendArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    tags = serializers.SerializerMethodField('get_translated_tags')
    categories = serializers.SerializerMethodField('get_translated_categories')
    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_translated_tags(self, obj):
        tags = Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = Category.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return CategorySerializer(categories, many=True).data


class SitemapUrlSerializer(TranslatableModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(TranslatableModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id', 'page', 'title', 'permalink')
