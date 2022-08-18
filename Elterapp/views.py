from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NFTSerializer
from .models import NFT
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class NFTViewSet(viewsets.ModelViewSet):
    serializer_class = NFTSerializer
    queryset = NFT.objects.all().order_by("date_of_creation")
    
    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raiseExceptions=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)