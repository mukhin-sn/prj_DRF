from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModer, IsMaster
from materials.models import Course
from users.models import Roles
from materials.serializers.courses_serializers import CourseSerializer, CreateCourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    dict_serializer = {
        'create': CreateCourseSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role != Roles.MODERATOR:
            queryset = queryset.filter(master=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(master=self.request.user)

    def get_serializer_class(self):
        return self.dict_serializer.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsMaster | IsModer]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsMaster | IsModer]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsMaster | IsModer]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsMaster]
        return [permission() for permission in self.permission_classes]
