from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    location = models.CharField(max_length=100,null=True)
    temperature = models.CharField(max_length=100,null=True)
    created = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(f"{self.host} {self.location}")