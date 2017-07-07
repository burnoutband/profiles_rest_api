# We Stores All of the permission classes for our application.

from rest_framework import permissions

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id



class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id




# class UserPermission(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         print(view.action)
#         print(request.user.is_superuser)
#         print(request.user.is_authenticated())
#
#         if view.action == 'list':
#             return request.user.is_authenticated() and request.user.is_superuser
#         elif view.action == 'create':
#             return True
#         elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
#             return True
#         else:
#             return False
#
#     def has_object_permission(self, request, view, obj):
#         print(view.action)
#         print(request.user.is_superuser)
#         print(request.user.is_authenticated())
#
#         if view.action == 'retrieve':
#             return request.user.is_authenticated() and (obj == request.user or request.user.is_superuser)
#         elif view.action in ['update', 'partial_update']:
#             return request.user.is_authenticated() and (obj == request.user or request.user.is_superuser)
#         elif view.action == 'destroy':
#             return request.user.is_authenticated() and request.user.is_superuser
#         else:
#             return False



# TODOdone  2017-07-06T21:12:12+09:00
    # user list -- for admin only
    # get/update user profile - only each user or admin
    # https://stackoverflow.com/questions/37642175/how-to-add-django-rest-framework-permissions-on-specific-method-only
    # https://stackoverflow.com/questions/19313314/django-rest-framework-per-action-permission

    # 자기자신꺼만 보인다.
