from django.db import models

# Create your models here.
class Chat(models.Model):
    text = models.CharField(max_length=100000000)
    time = models.CharField(max_length=100)
    