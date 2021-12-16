from .base import BaseModelSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class PermissionSerializer(BaseModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserProfileSerializer(BaseModelSerializer):

    user_permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserSerializer(BaseModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    repassword = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    level = serializers.CharField(required=False)
    has_token = serializers.SerializerMethodField("get_token", read_only=True)
    user_permissions = PermissionSerializer(read_only=True, many=True)

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
            "repassword",
            "level",
            "user_permissions",
            "has_token",
            "is_superuser",
        )

    def validate(self, data):
        new_password = data.get("password", "")
        if new_password and len(new_password) < 8:
            raise serializers.ValidationError(_("Passwords too short"))
        if new_password != data.get("repassword", ""):
            raise serializers.ValidationError(_("Passwords should match"))
        return data

    def create(self, validated_data):
        user = get_user_model()(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            level=validated_data["level"],
        )
        if validated_data.get("password", ""):
            user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.level = validated_data.get("level", instance.level)
        if validated_data.get("password", ""):
            instance.set_password(validated_data["password"])
        permissions = validated_data.get("user_permissions", [])
        instance.user_permissions.clear()
        for permission in permissions:
            instance.user_permissions.add(permission)
        instance.save()
        return instance
