from rest_framework.generics import ListAPIView, get_object_or_404
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
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     obj = serializer.save()
    #     # проверяем, если был введен пользоватяль, то подписка на введенного пользователя,
    #     # если нет - то подписка на авторизованного пользователя
    #     if not obj.user:
    #         obj.user = self.request.user
    #     obj.save()

    def post(self, *args, **kwargs):
        # получаем юзера из запроса
        user = self.request.user

        # получаем id курса из запроса
        course_id = self.request.data.get("course")

        # получаем данные о подписке (если подписки нет, то создаем подписку)
        course_item = get_object_or_404(Course, pk=course_id)
        subs_items, subs_value = Subscription.objects.get_or_create(user=user, course=course_item)
        if subs_value:
            message = "Подписка создана"
        else:
            subs_items.delete()
            message = "Подписка удалена"
        return Response({"message": message})


# class SubscriptionDestroyView(DestroyAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]
