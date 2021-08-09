from django.db import models
from django.contrib.auth.models import AbstractUser

# нужно в модель добавить био и роль и сделать их choice
class User(AbstractUser):
    bio = models.TextField(reqired=False)
    role = models.CharField(max_length=30, required=False)

    REQUIRED_FIELDS = ('username', 'email')
