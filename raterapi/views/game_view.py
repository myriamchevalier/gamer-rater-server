from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Game

class GameView(ViewSet):
    """Gamer Rater Games"""

    def list(self, request):
        """Handles GET request for all games

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all() # Gets all records from the db

        serializer = GameSerializer(games, many=True, context = {'request': request})
        return Response(serializer.data)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    
    Arguments:
        serializer type
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'estimated_time_to_play', 'age_recommendation', 'player')
        depth = 1