from rest_framework.permissions import BasePermission, DjangoModelPermissions


class PropUserPermission(BasePermission):
    prop = None

    def _process_permission(self, request, obj=None):
        assert self.prop is not None
        allowed_methods = set()

        if request.user.has_perm(f'core.change_user_{self.prop}'):
            allowed_methods.add('GET')
            allowed_methods.add('PUT')

        if request.user.has_perm(f'core.view_own_{self.prop}'):
            if not obj or obj == request.user:
                allowed_methods.add('GET')

        return request.method in allowed_methods

    def has_permission(self, request, view):
        return self._process_permission(request)

    def has_object_permission(self, request, view, obj):
        return self._process_permission(request, obj)


class SubordinatesPermission(PropUserPermission):
    prop = 'subordinates'


class SupervisorPermission(PropUserPermission):
    prop = 'supervisor'


class StructurePermission(DjangoModelPermissions):
    perms_map = {
        'GET': ['core.view_structure'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': [],
        'PUT': [],
        'PATCH': [],
        'DELETE': [],
    }


class UsersPermission(DjangoModelPermissions):
    perms_map = {
        'GET': ['core.view_user'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['core.add_user'],
        'PUT': ['core.change_user'],
        'PATCH': ['core.change_user'],
        'DELETE': ['core.delete_user'],
    }
