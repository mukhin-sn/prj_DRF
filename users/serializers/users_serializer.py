from rest_framework.serializers import ModelSerializer

from users.models import User
from users.serializers.payment_serializer import PaymentSerializer


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'city', 'payments')
