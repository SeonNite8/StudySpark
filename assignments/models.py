from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='assignments/')

    def __str__(self):
        return self.name
