from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Поьзователь'
        verbose_name_plural = 'Пользователи'
