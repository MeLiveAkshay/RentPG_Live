from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon=models.CharField(max_length=100, default='fa fa-cog')
    created_at = models.DateTimeField(auto_now_add=True)
   


class User(models.Model):
    name = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    icon = models.CharField(max_length=100, default='fa fa-user')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    present_address = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    parament_address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    