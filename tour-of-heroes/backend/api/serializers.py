from rest_framework import serializers

from app.models import HeroModel

class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = ("id", "name",)

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = ("id", "name",)

