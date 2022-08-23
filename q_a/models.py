from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User 

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField(null= True, blank=True, max_length=2000)
    image = models.ImageField(null= True, blank=True, upload_to='post_images')
    created_at = models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        return reverse('q_a:question-details', kwargs={'pk':self.pk})



    
    
