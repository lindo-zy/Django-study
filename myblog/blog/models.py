from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.TextField(max_length=2)

    def __str__(self):
        return self.name
