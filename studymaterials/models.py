from django.db import models

class StudyMaterial(models.Model):
    SUBJECT_CHOICES = [
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
    ]

    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='study_materials/')
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES,default='physics')

    def __str__(self):
        return self.title
