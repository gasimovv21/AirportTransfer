from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        null=True,
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            )
        ]