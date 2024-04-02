from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Subscription, Course
from materials.serializers.subscription_serializers import SubscriptionSerializer


class SubscriptionListView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionAPIView(APIView):
    # serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     obj = serializer.save()
    #     # проверяем, если был введен пользоватяль, то подписка на введенного пользователя,
    #     # если нет - то подписка на авторизованного пользователя
    #     if not obj.user:
    #         obj.user = self.request.user
    #     obj.save()

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)
        subscription, subs_items = Subscription.objects.get_or_create(user=user, course=course_item)
        if subs_items.exists():
            message = "Подписка удалена"
        else:
            message = "Подписка создана"
        return Response({"message": message})


class SubscriptionDestroyView(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
