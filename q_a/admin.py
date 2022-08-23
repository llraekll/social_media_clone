from django.contrib import admin
from .models import Question, Answer

# Register your models here.


#Models registered will be available on the admin site 
admin.site.register(Question)
admin.site.register(Answer)