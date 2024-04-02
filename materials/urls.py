from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views.lessons import (LessonCreateView, LessonListView, LessonUpdateView, LessonRetrieveView,
                                     LessonDestroyView)
from materials.views.courses import CourseViewSet
from materials.views.subscription import SubscriptionListView, SubscriptionAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [

    path('lesson/', LessonListView.as_view(), name='lessons'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),

    path('subscription/', SubscriptionListView.as_view(), name='subscription'),
    path('subscription/create/', SubscriptionAPIView.as_view(), name='subscription_create'),
    # path('subscription/delete/<int:pk>/', SubscriptionDestroyView.as_view(), name='subscription_delete'),

] + router.urls
