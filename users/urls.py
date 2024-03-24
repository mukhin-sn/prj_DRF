from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.payments import PaymentListView
from users.views.users import UserCreateView, UserListView, UserRetrieveView, UserUpdateView, UserDestroyView
# from users.views.users import UserViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r'user', UserViewSet)

urlpatterns = [
    path('payment/', PaymentListView.as_view(), name='payments'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('retrieve/<int:pk>/', UserRetrieveView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('destroy/<int:pk>/', UserDestroyView.as_view(), name='user_destroy'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]    # + router.urls
