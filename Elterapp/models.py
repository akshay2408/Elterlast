from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_wallet = models.CharField(max_length=40)


class Collection(models.Model):
    id = models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    

class NFT(models.Model):
    asset_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    picture = models.URLField()
    external_link = models.URLField()
    description = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    supply = models.IntegerField()
    royalties = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_creation = models.DateField(auto_now=True)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT)
    
    