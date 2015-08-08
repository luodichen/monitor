from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()
    token = models.TextField()
    creat_time = models.IntegerField()
    last_active_time = models.IntegerField(default=0)
    last_active_ip = models.TextField(null=True)
