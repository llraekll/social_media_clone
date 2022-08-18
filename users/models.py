from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profile_image', default='-9g1w51.jpg.jpg')
    bio = models.CharField(max_length=1000)
    mobile_no = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - Profile'