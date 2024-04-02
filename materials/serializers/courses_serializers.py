from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.serializers.lessons_serializers import LessonSerializer


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    subs_course = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_subs_course(self, obj):
        queryset = Subscription.objects.filter(course=obj.course)
        return Subscription.objects.filter(course=obj['id'])

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'preview', 'master', 'count_lessons', 'lessons', 'subs_course')
        # fields = "__all__"


class CreateCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
