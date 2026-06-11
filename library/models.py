from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='library_resources/')

    subject = models.ForeignKey(subject,on_delete=models.CASCADE,related_name='resources')

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('library-home')