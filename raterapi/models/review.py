from django.db import models

from raterapi.models import player

class Review(models.Model):
    content = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

    