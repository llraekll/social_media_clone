from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField() 
    created_at=models.DateTimeField(default=datetime.now)
    profileimg = models.ImageField(
        upload_to='profile_image', default='default_profile_image.jpg')

    def __str__(self):
        return self.user.username