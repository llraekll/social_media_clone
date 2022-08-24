from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User 

# Create your models here.

# Models have to be registered in admin.py for access on admin site

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField(null= True, blank=True, max_length=2000)
    image = models.ImageField(null= True, blank=True, upload_to='post_images')
    created_at = models.DateTimeField(default=datetime.now)
    votes = models.ManyToManyField(User, related_name='question_post')
    

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        return reverse('q_a:question-details', kwargs={'pk':self.pk})

    def total_votes(self):
        return self.votes.count()

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)

    content = models.TextField(null=True, blank=True)
    created_at= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_absolute_url(self):
        return reverse('q_a:question-details', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
    
