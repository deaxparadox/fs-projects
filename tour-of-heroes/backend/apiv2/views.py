from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def v2_not_implemented(request):
    return Response({}, status=status.HTTP_501_NOT_IMPLEMENTED)