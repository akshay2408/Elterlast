import pytest
from django.contrib.auth.models import User
from Elterapp.models import Wallet, Collection, NFT


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def user():
    user = User.objects.get_or_create(
        username="Akshay",
        is_staff=True,
        is_superuser=True,
        email='akshay@gmail.com', 
        )
    return user


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def wallet(user):
    wallet = Wallet.objects.get_or_create(
        user=user,
        user_wallet="100"
    )
    return wallet


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def collection(user):
    Collection.objects.bulk_create(
        [
            Collection(
                name="collection1",
                discription="test discription1",
                creator=user
                ),
            Collection(
                name="collection2",
                discription="test discription2",
                creator=user
                ),
        ]
    )
    return Collection.objects.all()


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def nft(user,collection):
    NFT.objects.bulk_create(
        [
            NFT(
                name="test nft1",
                picture= "test.com",
                external_link="test.com",
                description="test discription for nft",
                collection=collection[0],
                supply=1,
                royalties=10,
                buyer=user
                ),
            NFT(
                name="test nft2",
                picture= "test.com",
                external_link="test.com",
                description="test discription for nft",
                collection=collection[1],
                supply=1,
                royalties=10,
                buyer=user
                ),
            NFT(
                name="test nft3",
                picture= "test.com",
                external_link="test.com",
                description="test discription for nft",
                collection=collection[0],
                supply=1,
                royalties=10,
                buyer=user
                ),
            NFT(
                name="test nft4",
                picture= "test.com",
                external_link="test.com",
                description="test discription for nft",
                collection=collection[1],
                supply=1,
                royalties=10,
                buyer=user
                ),
            NFT(
                name="test nft5",
                picture= "test.com",
                external_link="test.com",
                description="test discription for nft",
                collection=collection[0],
                supply=1,
                royalties=10,
                buyer=user
                ),
        ]
    )
    return NFT.objects.all()


