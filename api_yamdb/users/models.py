from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from django.core.mail import send_mail

# список ролей пользователя
from api_yamdb.settings import ROLES


class MyUserManager(UserManager):
    '''Менеджер позволяет сохранять superuser
    с полями username и email'''
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if username == 'me':
            raise ValueError('The name "me" is forbidden to use')
        # send_mail(subject='Subject', message='Message', from_email='frommail@mail.ru', recipient_list=[email],
        #       fail_silently=False)
        return super().create_user(username, email=email, password=password, **extra_fields)


    def create_superuser(self, username, email, password, **extra_fields):
        # сохраняем суперпользователя с ролью admin
        user = self.create_user(password, username=username, email=email, role='admin')
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')
    password = None
    objects = MyUserManager()

    REQUIRED_FIELDS = ('email', )

