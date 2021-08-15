# список ролей пользователя
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# список ролей пользователя
from api_yamdb.settings import (ROLES, MESSAGE_FOR_RESERVED_NAME,
                                RESERVED_NAME)


class MyUserManager(UserManager):
    """Сохраняет пользователя только с email.
    Зарезервированное имя использовать нельзя."""
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле email обязательное')
        if username == RESERVED_NAME:
            raise ValueError(MESSAGE_FOR_RESERVED_NAME)
        return super().create_user(
            username, email=email, password=password, **extra_fields)

    def create_superuser(
            self, username, email, password, role=ROLES[2][0], **extra_fields):
        return super().create_superuser(
            username, email, password, role=ROLES[2][0], **extra_fields)


class User(AbstractUser):
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')
    objects = MyUserManager()

    REQUIRED_FIELDS = ('email', 'password')
