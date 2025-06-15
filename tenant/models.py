from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='tenant_profile_pictures/', blank=True, null=True)
    domain = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)