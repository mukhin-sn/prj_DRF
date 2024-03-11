from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [] + router.urls
