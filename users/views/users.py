from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.users_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
