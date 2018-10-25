from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        verbose_name='Nome',
        max_length=150
    )

    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'