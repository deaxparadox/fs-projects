from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import HeroModel
from .serializers import HeroesSerializer

@api_view(http_method_names=["GET"])
def get_heroes(request):
    heroes = HeroModel.objects.all()
    serializer = HeroesSerializer(heroes, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_hero(request, id: int | None = None):
    if not id:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    heroes = HeroModel.objects.get(id=id)
    serializer = HeroesSerializer(heroes)    
    return Response(serializer.data, status=status.HTTP_200_OK)