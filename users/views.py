from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# custom permission class (example)
class IsAdminOrSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the user themselves or admin
        return obj == request.user or request.user.is_staff


class UserViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]

    def list(self, request):
        # only admin users can access the list of users
        if request.user.is_staff:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        # allow any authenticated user to create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        self.check_object_permissions(request, user)
        return Response(serializer.data)
