from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.CharField(max_length=4000)
    post_image = models.ImageField(upload_to="post_image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
