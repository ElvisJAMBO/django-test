from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Student, Task, Schedule, Teacher, Course
from .serializers import StudentSerializer, TaskSerializer, ScheduleSerializer, TeacherSerializer, CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'name']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # Autorise tout le monde à voir, mais demande d'être connecté pour créer/modifier
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # On active le filtrage ici
    filter_backends = [DjangoFilterBackend]
    # On définit les champs filtrables
    filterset_fields = ['student', 'week_number', 'day']

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'name', 'matricule']

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher', 'name']