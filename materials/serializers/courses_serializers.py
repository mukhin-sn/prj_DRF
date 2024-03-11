from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson
from materials.serializers.lessons_serializers import LessonSerializer


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source='lessons_set', many=True, read_only=True)

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'preview', 'count_lessons', 'lessons')
        # fields = "__all__"
