from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    department = models.ForeignKey(Department, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
