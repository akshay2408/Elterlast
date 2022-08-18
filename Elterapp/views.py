from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NFTSerializer
from .models import NFT

# Create your views here.

class NFTViewSet(viewsets.ModelViewSet):
    serializer_class = NFTSerializer
    queryset = NFT.objects.all().order_by("date_of_creation")
    