from rest_framework import permissions


class HasSelfVotedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the owner
        return obj.up_vote_by == request.user or obj.down_vote_by == request.user
