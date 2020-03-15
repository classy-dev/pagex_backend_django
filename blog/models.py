from django.db import models
from django.conf import settings


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title
