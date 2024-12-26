from rest_framework import permissions

class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.is_staff or hasattr(request.user, 'vendor'))

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if hasattr(request.user, 'vendor'):
            return obj.vendor == request.user.vendor
        return request.method in permissions.SAFE_METHODS