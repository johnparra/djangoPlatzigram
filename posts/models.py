from django.db import models


class User(models.Model):
    email = models.EmailField()
    password: str = models.CharField(max_length=8)

    first_name: str = models.CharField(max_length=20)
    last_name: str = models.CharField(max_length=20)

    bio = models.TextField()

    birthdate = models.DateField()

    created = models.DateField()
    modified = models.DateField()