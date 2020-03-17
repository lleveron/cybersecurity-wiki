from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from PIL import Image


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='article.jpg', upload_to='article_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs,):
    #    super().save(*args, **kwargs)

    #   img = Image.open(self.image.path)

    #    if img.width >= 1920 and img.height > 700:
    #        croppedimg = img.crop((0,0,1920,700))
    #        croppedimg.save(self.image.path)
    #    elif img.width <= 1920 and img.height > 700:
    #        croppedimg = img.crop((0,img.width*0.32,img.width,img.width*0.68))
    #        croppedimg.save(self.image.path)
    #    elif img.width <= 1920 and img.height < 700:
    #        croppedimg = img.crop((0,0,img.width,img.height))
    #        croppedimg.save(self.image.path)
    #    elif img.width >= 1920 and img.height < 700:
    #        croppedimg = img.crop((0,0,1920,img.height))
    #        croppedimg.save(self.image.path)
    #    else:
    #        img.save(self.image.path)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})