from rest_framework import permissions


class CamomillaBasePermissions(permissions.BasePermission):

    def _check_custom_permissions(self, request, model):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            permission = ''
            model_name = model.__name__.lower()
            if request.method == 'GET':
                permission = 'read'
            if request.method == 'DELETE':
                permission = 'delete'
            if request.method == 'POST':
                permission = 'add'
            if request.method in ['PUT', 'PATCH']:
                permission = 'change'
            perm = '{0}.{1}_{2}'.format(
                model._meta.app_label, permission, model_name
            )
            return request.user.has_perm(perm)

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.level == '3':
            return True
        else:
            return self._check_custom_permissions(request, view.model)

        return False

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False

        if request.user.level == '3':
            return True
        else:
            return self._check_custom_permissions(request, view.model)

        return False


class CamomillaSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.level == '3'

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.level == '3'
