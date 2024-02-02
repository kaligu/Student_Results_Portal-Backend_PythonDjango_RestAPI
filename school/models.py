from django.db import models

class School(models.Model):
    id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
