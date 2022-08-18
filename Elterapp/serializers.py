from rest_framework import serializers
from . models import NFT


class NFTSerializer(serializers.Serializer):
    class Meta:
        model = NFT
        feilds = "__all__"