from django.db import models

class AdminMemberModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='admin')  # ✅ Added role
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Fixed

    def __str__(self):
        return self.name
