from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TaskViewSet, ScheduleViewSet, TeacherViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]