from rest_framework import serializers
from games.models import (
    Game
)


class GameSerializer(serializers.ModelSerializer):
    game_slug = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = ['name','game_slug']
    
    def get_game_slug(self,obj):
        return obj.get_absolute_url()




