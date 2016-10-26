from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow superusers to edit objects.
    """

    def has_permission(self, request, view):
         # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # You need to be superuser to do POST, PUT and PATCH requests.
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # You need to be superuser to do POST, PUT and PATCH requests.
        return request.user.is_superuser