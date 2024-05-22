from django.db import models

# Create your models here.

class Task(models.Model):
    taskPriority = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    taskStatus = [
        (True, 'Completed'),
        (False, 'Uncompleted'),
    ]

    taskID = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    teacherName = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices = taskPriority)
    description = models.TextField(max_length=1000)
    createdBy = models.CharField(max_length=100)
    status = models.BooleanField(default=False, choices = taskStatus)

    def str(self):
        return self.title

    class Meta:
        ordering = ['taskID']
