from django.urls import path, include
from rest_framework import routers
from .views import NFTViewSet


router = routers.DefaultRouter()
router.register('NFT', NFTViewSet)


urlpatterns = [
    path('v1/', include(router.urls))
]