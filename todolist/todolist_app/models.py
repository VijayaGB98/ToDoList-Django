from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low'),
    )
    STATUS = (
        ('Incomplete', 'Incomplete'),
        ('Complete', 'Complete'),
    )
    task_name = models.CharField(max_length=500)
    priority = models.CharField(max_length=255, choices=PRIORITY, default='Low')
    status = models.CharField(max_length=255, choices=STATUS, default='Incomplete')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name