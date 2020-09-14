from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low'),
    )
    task_name = models.CharField(max_length=500)
    priority = models.CharField(max_length=255, choices=PRIORITY)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name