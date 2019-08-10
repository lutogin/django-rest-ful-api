from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
"""Импортируем базовую абстрактную модель базового пользователя django, менеджера пользователейб и модуль прав"""


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        """self.normalize_email(email) для привидепния email в правильный вид(lower_case)"""
        user.set_password(password)
        """Password make a encrypted"""
        user.save(using=self._db)
        """using=self._db для работы с нексолькими базами, но хорошая практика указывать его всегда"""

        return user

    def create_superuser(self, email, password):
        """Creates and saves new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
