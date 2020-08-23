from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/') #location for the images
    summary = models.CharField(max_length=200)