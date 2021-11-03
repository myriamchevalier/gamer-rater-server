from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    """Model for players, using User model from auth"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)