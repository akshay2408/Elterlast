from django.contrib import admin
from .models import Wallet, Collection, NFT
# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    fields = ["user", "user_wallet"]

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    fields = ["name", "discription", "creator"]