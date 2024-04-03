from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.paginators import MaterialsPaginator
from materials.serializers.lessons_serializers import LessonSerializer
from users.models import Roles
from users.permissions import IsModer, IsMaster


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.master = self.request.user
        obj.save()


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMaster | IsModer]
    pagination_class = MaterialsPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role != Roles.MODERATOR:
            queryset = queryset.filter(master=self.request.user)
        return queryset


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMaster | IsModer]


class LessonRetrieveView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMaster | IsModer]


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsMaster]
