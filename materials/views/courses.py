from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers.courses_serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = ['IsAuthenticated']
        elif self.action == 'list':
            self.permission_classes = ['IsAuthenticated']
        elif self.action == 'retrieve':
            self.permission_classes = ['IsAuthenticated', 'IsModer']
        elif self.action == 'update':
            self.permission_classes = ['IsAuthenticated', 'IsModer']
        elif self.action == 'destroy':
            self.permission_classes = ['IsAuthenticated']
        return [permission for permission in self.permission_classes]
