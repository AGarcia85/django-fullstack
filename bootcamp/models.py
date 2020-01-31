from django.db import models
from datetime import date

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField(null=True)
    immersive = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='posts', null=True)
    post = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.post