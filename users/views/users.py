from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.users_serializer import UserSerializer, CreateUserSerializer


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
