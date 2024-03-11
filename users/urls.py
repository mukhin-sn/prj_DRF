from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views.payments import PaymentListView
from users.views.users import UserViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('payment/', PaymentListView.as_view(), name='payments'),

    ] + router.urls
