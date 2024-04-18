from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
    
    def has_permission(self, request, view):
        if request.method == 'POST': 
            return request.user.is_staff 
        return True


class IsStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
