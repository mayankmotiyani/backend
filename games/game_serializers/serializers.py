from rest_framework import serializers
from games.models import (
    GameCategory
)


class GameCategorySerializer(serializers.ModelSerializer):
    game_slug = serializers.SerializerMethodField()
    class Meta:
        model = GameCategory
        fields = ['name','game_slug']
    
    def get_game_slug(self,obj):
        return obj.get_absolute_url()




