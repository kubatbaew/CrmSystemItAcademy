from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.mentors.models import Mentor

class IsManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
    
    def has_permission(self, request, view):
        if request.method == 'POST': 
            return request.user.is_superuser 
        return True


class IsStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True


class IsMentor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return bool(obj.mentor.username == request.user.username)

    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE', 'PUT', 'PATCH']:
            return request.user.is_superuser
        return True
