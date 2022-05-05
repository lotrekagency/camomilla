from django.forms import ValidationError
from .base import BaseModelSerializer
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import Permission
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class PermissionSerializer(BaseModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserProfileSerializer(BaseModelSerializer):

    user_permissions = PermissionSerializer(read_only=True, many=True)
    password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    repassword = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )

    class Meta:
        model = get_user_model()
        fields = "__all__"

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate_repassword(self, value):
        if "password" in self.initial_data:
            if not value:
                raise ValidationError(_("This field is required"))
            if self.initial_data["password"] != value:
                raise ValidationError(_("Passwords do not match."))
        return value

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        if "password" in validated_data:
            user.set_password(validated_data["password"])
            user.save()
        return user


class UserSerializer(BaseModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    level = serializers.CharField(required=False)
    has_token = serializers.SerializerMethodField("get_token", read_only=True)

    def get_token(self, obj):
        return hasattr(obj, "auth_token")

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "level",
            "user_permissions",
            "has_token",
            "is_superuser",
        )

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        if "password" in validated_data:
            user.set_password(validated_data["password"])
            user.save()
        return user
