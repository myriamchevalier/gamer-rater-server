from django.db import models

class Screenshot(models.Model):
    uploaded_picture = models.ImageField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    