from django.db import models
from django.conf import settings


# Create your models here.
class Passion(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_images/user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(blank=True, null=True, upload_to=user_directory_path)
    passion = models.ForeignKey(Passion, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.user.email})'
