from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.task
