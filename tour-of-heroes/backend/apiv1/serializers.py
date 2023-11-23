
from rest_framework import serializers

from app.models import HeroModel

class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = ("id", "name",)

class HeroAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        # fields = ("id", "name",)
        exclude = ["id",]

    # def create(self, validated_data):
    #     new_hero_id = HeroModel.objects.all().order_by("id").last().id + 1
    #     new_hero: HeroModel = HeroModel.objects.create(
    #         name=validated_data.get('name")'),
    #         id=new_hero_id
    #     )
    #     return new_hero
    
