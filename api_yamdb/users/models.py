from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# список ролей пользователя
from api_yamdb.settings import ROLES


class MyUserManager(UserManager):
    '''Сохраняет пользователя только с email.
    Нельзя использовать слово me для имени пользователя.'''
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if username == 'me':
            raise ValueError('The name "me" is forbidden to use')
        return super().create_user(username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email, password, role, **extra_fields):
        return super().create_superuser(username, email, password, role=ROLES[2][0], **extra_fields)


class User(AbstractUser):
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')
    objects = MyUserManager()

    REQUIRED_FIELDS = ('email', 'password')

