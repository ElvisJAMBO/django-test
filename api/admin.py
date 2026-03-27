from django.contrib import admin
from .models import Student, Task, Schedule, Teacher, Course

admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Schedule)
admin.site.register(Teacher)
admin.site.register(Course)
