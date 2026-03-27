from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Image de profil de l'élève
    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Lundi'),
        ('TUE', 'Mardi'),
        ('WED', 'Mercredi'),
        ('THU', 'Jeudi'),
        ('FRI', 'Vendredi'),
        ('SAT', 'Samedi'),
        ('SUN', 'Dimanche'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='schedules')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    week_number = models.PositiveIntegerField() # Pour trier par semaine
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        # Trie par semaine, puis par jour, puis par heure
        ordering = ['week_number', 'day', 'start_time']

    def __str__(self):
        return f"{self.student.name} - {self.day} (Semaine {self.week_number})"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=100)
    # Image de profil de l'enseignant
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)

    class Meta:
        # Trie par nom
        ordering = ['name']

    def __str__(self):
        return self.teacher.name