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
        queryset = Subscription.objects.filter(course=obj)
        if queryset:
            return 'Подписка на курс оформлена'

        # Subscription.objects.filter(course=obj['id'])
        return 'Подписка на курс удалена'

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'preview', 'master', 'count_lessons', 'subs_course', 'lessons')
        # fields = "__all__"


class CreateCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
