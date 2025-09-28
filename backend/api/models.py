from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return self.team_name