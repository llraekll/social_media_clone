from django.db import models
import uuid
from datetime import datetime

# Create your models here.


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.TextField(max_length=700)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(default=datetime.now)
    up_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class UpVote(models.Model):
    query_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class DownVote(models.Model):
    query_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
