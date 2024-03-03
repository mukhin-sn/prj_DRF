from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views.lessons import (LessonCreateView, LessonListView, LessonUpdateView, LessonRetrieveView,
                                     LessonDestroyView)
from materials.views.courses import CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListView.as_view()),
    path('lesson/create/', LessonCreateView.as_view()),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view()),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view()),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view()),

] + router.urls
