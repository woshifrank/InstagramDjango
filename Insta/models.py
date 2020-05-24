from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality' : 100},
        blank = True,
        null = True
    )
    # after each Post creation/edit, call this function and jump to the post detail page
    def get_absolute_url(self):
        # reverse url
        return reverse("post_detail",args=[str(self.id)])

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality' : 100},
        blank = True,
        null = True
    )
