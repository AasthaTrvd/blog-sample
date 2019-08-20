from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # reverse() funtion returns route as a string
    # rediret() funtion redirects to route
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pics is a folder to store uploaded pics
    image = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username + " " + "Profile"

    # function to resize image
    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  # specify image size
            img.thumbnail(output_size)
            img.save(self.image.path)  # overite existing image size with latest image
