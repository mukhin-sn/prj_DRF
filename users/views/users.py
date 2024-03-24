from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsUser, IsOwner
from users.serializers.users_serializer import UserSerializer, CreateUserSerializer, GeneralUserSerializer


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GeneralUserSerializer
    permission_classes = [AllowAny]


class UserCreateView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(self.request.data["password"])
        new_user.save()


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GeneralUserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def perform_update(self, serializer):
        user = serializer.save()
        try:
            user.set_password(self.request.data["password"])
        except KeyError:
            pass
        user.save()


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = GeneralUserSerializer
    permission_classes = [IsAuthenticated, IsUser]
