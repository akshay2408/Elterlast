from distutils.command.clean import clean
import pytest
from rest_framework.test import APIClient
from Elterlast import settings


BASE_URL = settings.BASE_URL

class TestWallet:
    @pytest.mark.django_db(transaction=True)
    def test_model(self,wallet, user):
        inst = wallet
        assert inst.pk > 0
        assert inst.user == user
        inst.save()
        inst.delete()



class TestCollection:
    @pytest.mark.django_db(transaction=True)
    def test_model(self,collection, user):
        inst = collection
        assert inst[0].pk > 0
        assert inst[0].creator == user
        inst.save()
        inst.delete()


class TestNFT:
    @pytest.mark.django_db(transaction=True)
    def test_model(self,NFT,collection, user):
        inst = NFT
        assert inst[0].pk > 0
        inst.save()
        inst.delete()


class TestNFTViewSet:
    
    @pytest.mark.django_db(transaction=True)
    def test_create(self, user, collection):
        url = BASE_URL + 'nft-api/v1/NFT/'
        client = APIClient()
        data = {
            "name":"nft1",
            "picture":"test.com",
            "external_link":"test.com",
            "description":"test discription",
            "collection":collection[0].id,
            "supply":1,
            "royalties":1.0,
            "buyer":user.id,
        }
        res = client.post(url, data=j, content_type='application/json')
        assert res.status_code == 200
        data = res.json()
        print(data)

    @pytest.mark.django_db(transaction=True)
    def test_get_by_id(self, nft):
        nft_id = nft[0].asset_id
        url = BASE_URL + f'nft-api/v1/NFT/{nft_id}'
        client = APIClient()
        res = client.get(url)
        assert res.status_code == 200
        data = res.json()
        print(data)
    
    @pytest.mark.django_db(transaction=True)
    def test_getall(self, nft):
        url = BASE_URL + f'nft-api/v1/NFT/'
        client = APIClient()
        res = client.get(url)
        assert res.status_code == 200
        data = res.json()
        print(data)
