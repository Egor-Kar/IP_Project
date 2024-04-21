
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        'MyUser', models.CASCADE, related_name='profile',
        verbose_name='Пользователь', primary_key=True,
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.user} ({self.pk})'