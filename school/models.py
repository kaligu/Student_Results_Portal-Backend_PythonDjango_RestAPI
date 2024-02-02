from django.db import models

class School(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.id + ' ' + self.name
