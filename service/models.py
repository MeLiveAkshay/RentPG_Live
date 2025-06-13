from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon=models.CharField(max_length=100, default='fa fa-cog')
    created_at = models.DateTimeField(auto_now_add=True)
   
