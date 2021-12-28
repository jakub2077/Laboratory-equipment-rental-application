from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    if user.is_superuser:
        return True
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class AdminPermission(BasePermission):
    required_groups = ['admin']
    
    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class TeacherPermission(BasePermission):
    required_groups = ['Teacher','admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class StudentPermission(BasePermission):
    required_groups = ['Student', 'Teacher', 'admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission