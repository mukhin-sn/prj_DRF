from rest_framework.serializers import ModelSerializer, CharField
# from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.validators import validate_link_to_video


class LessonSerializer(ModelSerializer):
    link_to_video = CharField(validators=[validate_link_to_video])

    class Meta:
        model = Lesson
        fields = '__all__'
        # permission_classes = [IsAuthenticated]
