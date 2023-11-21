from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import HeroModel
from .serializers import HeroSerializer

@api_view()
def get_heroes(request):
    heroes = HeroModel.objects.all()
    serializer = HeroSerializer(heroes, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)