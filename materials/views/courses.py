from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsModer, IsMaster
from materials.models import Course
from materials.serializers.courses_serializers import CourseSerializer, CreateCourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    dict_serializer = {
        'create': CreateCourseSerializer,
    }

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
