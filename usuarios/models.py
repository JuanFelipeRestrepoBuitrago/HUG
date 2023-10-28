from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    institution = models.CharField(max_length=500)
    user_type = models.CharField(max_length=5, default='user', choices=(('user', 'user'), ('admin', 'admin')))

    def __str__(self):
        return self.username
