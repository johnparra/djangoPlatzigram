from django.db import models


class User(models.Model):
    email = models.EmailField()
    password: str = models.CharField(max_length=8)

    first_name: str = models.CharField(max_length=100)
    last_name: str = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email