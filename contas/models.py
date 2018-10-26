from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):

    custom_email = models.EmailField(
        verbose_name='Usuário / E-mail',
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'},
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150,
        validators=[UnicodeUsernameValidator()], verbose_name='Apelido'
    )

    USERNAME_FIELD = 'custom_email'
    REQUIRED_FIELDS = ['username', 'email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'