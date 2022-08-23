from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profile_image', default='-9g1w51.jpg')
    bio = models.CharField(max_length=1000)
    mobile_no = models.IntegerField(null= True, blank=True)

    def __str__(self):
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.profileimg.path)
        if img.height > 300 or img.width > 300:
            ouput_size = (300, 300)
            img.thumbnail(ouput_size)
            img.save(self.profileimg.path)