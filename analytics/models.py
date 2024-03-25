from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class TestScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test1 = models.FloatField(null=True, blank=True)
    test2 = models.FloatField(null=True, blank=True)
    test3 = models.FloatField(null=True, blank=True)
    test4 = models.FloatField(null=True, blank=True)
    test5 = models.FloatField(null=True, blank=True)
