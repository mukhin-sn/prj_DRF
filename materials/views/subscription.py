from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from materials.serializers.subscription_serializers import SubscriptionSerializer


class SubscriptionCreateView(CreateAPIView):
    serializer_class = SubscriptionSerializer
