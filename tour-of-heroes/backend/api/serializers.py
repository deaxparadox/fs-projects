from rest_framework import serializers

from app.models import HeroModel

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = ("hero_id", "name",)