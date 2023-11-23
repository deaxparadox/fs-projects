from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import HeroModel
from .serializers import ( 
    HeroesSerializer, 
    HeroAddSerializer
)

@api_view(http_method_names=["GET"])
def get_heroes(request):
    name = request.GET.get("name")
    if name:
        hero: HeroModel | None = None        
        try:
            hero = HeroModel.objects.get(name__startswith=name)
        except HeroModel.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        if not hero:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeroesSerializer(hero)    
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    heroes = HeroModel.objects.all().order_by("-id")
    serializer = HeroesSerializer(heroes, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_hero(request, id: int | None = None):
    if not id:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    heroes = HeroModel.objects.get(id=id)
    serializer = HeroesSerializer(heroes)    
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(http_method_names=["POST"])
def add_hero(request):
    
    serializer = HeroAddSerializer(data=request.data)

    if serializer.is_valid():
        
        # generate new hero id
        new_hero_id = HeroModel.objects.all().order_by("id").last().id + 1
        serializer.save(id=new_hero_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # if serializers is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

