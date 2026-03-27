from rest_framework import serializers
from .models import Student, Task, Schedule, Teacher, Course

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']

class ScheduleSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    task_title = serializers.ReadOnlyField(source='task.title')
    
    # Ces champs servent à la CRÉATION (POST)
    student_id = serializers.IntegerField(write_only=True)
    task_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'student_id', 'task_id', 'student_name', 'task_title', 'day', 'week_number', 'start_time', 'end_time']

    def create(self, validated_data):
        # On récupère les IDs et on crée l'objet
        student = Student.objects.get(id=validated_data.pop('student_id'))
        task = Task.objects.get(id=validated_data.pop('task_id'))
        return Schedule.objects.create(student=student, task=task, **validated_data)

class StudentSerializer(serializers.ModelSerializer):
    # On affiche tous les horaires liés à cet élève (grâce au related_name='schedules')
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'photo', 'schedules']

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.ReadOnlyField(source='teacher.name')

    teacher_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Course
        fields = ['id', 'teacher_id', 'name', 'teacher_name']

    def create(self, validated_data):
        # On récupère les IDs et on crée l'objet
        teacher = Teacher.objects.get(id=validated_data.pop('teacher_id'))
        return Course.objects.create(teacher=teacher, **validated_data)

class TeacherSerializer(serializers.ModelSerializer):
    # On affiche tous les cours liés à cet enseignant (grâce au related_name='courses')
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'matricule', 'photo', 'courses']