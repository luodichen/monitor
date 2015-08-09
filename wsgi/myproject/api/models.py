from django.db import models

# Create your models here.

class DNSPodDomain(models.Model):
    domain = models.TextField()
    domain_id = models.TextField()

class User(models.Model):
    name = models.TextField()
    token = models.TextField()
    creat_time = models.IntegerField()
    last_active_time = models.IntegerField(default=0)
    last_active_ip = models.TextField(null=True)
    
    ddns_ip = models.TextField(null=True)
    sub_domain = models.TextField(null=True)
    sub_domain_id = models.TextField(null=True)
    domain = models.ForeignKey(DNSPodDomain, null=True)
    ddns_update_time = models.IntegerField(default=0)

class DNSPodAccount(models.Model):
    username = models.TextField()
    password = models.TextField()
