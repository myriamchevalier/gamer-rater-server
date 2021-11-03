from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    designer = models.CharField(max_length=60)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

    def __str__(self):
        return self.title