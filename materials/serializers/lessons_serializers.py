from rest_framework.serializers import ModelSerializer
# from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        # permission_classes = [IsAuthenticated]
