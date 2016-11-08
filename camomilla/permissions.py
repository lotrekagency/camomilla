from rest_framework import permissions


class CamomillaBasePermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated():
            return False

        if request.user.profile.level == '1':
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return False

        if request.user.profile.level == '2':
            return True

        if request.user.profile.level == '3':
            return True

        return False

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated():
            return False

        if request.user.profile.level == '1':
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return False

        if request.user.profile.level == '2':
            return True

        if request.user.profile.level == '3':
            return True

        return False


class CamomillaSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.level == '3'

    def has_object_permission(self, request, view, obj):
        return request.user.profile.level == '3'
