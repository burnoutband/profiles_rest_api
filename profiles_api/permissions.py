# We Stores All of the permission classes for our application.

from rest_framework import permissions


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




# TODO  2017-07-06T21:12:12+09:00
    # user list -- for admin only
    # get/update user profile - only each user or admin
    # https://stackoverflow.com/questions/37642175/how-to-add-django-rest-framework-permissions-on-specific-method-only
    # https://stackoverflow.com/questions/19313314/django-rest-framework-per-action-permission
