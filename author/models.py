from django.db import models
from django.conf import settings


# Create your models here.
class Passion(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField()
    passion = models.OneToOneField(Passion, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.user.email})'
