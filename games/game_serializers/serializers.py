from rest_framework import serializers
from games.models import (
    Game,
    GameSection2,
    GameSection3,
    ModernSolutionForVariousPlatform
)

class GameSerializer(serializers.ModelSerializer):
    game_slug = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = ['name','game_slug']
    
    def get_game_slug(self,obj):
        return obj.get_absolute_url()

class GameSection2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameSection2
        fields = "__all__"

class GameSection3Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameSection3
        fields = "__all__"

class ModernSolutionForVariousPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModernSolutionForVariousPlatform
        fields = "__all__"


class SingleGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
    
    def to_representation(self, obj):
        instance = super(SingleGameSerializer, self).to_representation(obj)
        instance['Section1'] = ModernSolutionForVariousPlatformSerializer(ModernSolutionForVariousPlatform.objects.get(game_id=instance['id'])).data
        instance['Section2'] = GameSection2Serializer(GameSection2.objects.filter(game_id=instance['id']),many=True).data
        instance['Section3'] = GameSection3Serializer(GameSection3.objects.filter(game_id=instance['id']),many=True).data
        return instance
    


