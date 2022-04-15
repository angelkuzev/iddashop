from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from iddashop.accounts.models import IddashopUser
from iddashop.common.validators import validate_phone_num


class Item(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 200
    DESCRIPTION_MIN_LENGTH = 2

    picture = models.ImageField()

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        )
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.01),
        )
    )


class Quantity(models.Model):
    s_size_quantity = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    m_size_quantity = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    l_size_quantity = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Order(models.Model):
    CLIENT_ADDRESS_MAX_LENGTH = 256
    CLIENT_PHONE_NUM_MAX_LENGTH = 10

    ordered_by = models.ForeignKey(
        IddashopUser,
        on_delete=models.PROTECT
    )

    ordered_on = models.DateTimeField(
        auto_now_add=True,
    )

    accepted_by = models.IntegerField(
        null=True,
        blank=True,
    )
    accepted_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    client_address = models.CharField(
        max_length=CLIENT_ADDRESS_MAX_LENGTH
    )

    client_phone_num = models.CharField(
        max_length=CLIENT_PHONE_NUM_MAX_LENGTH,
        validators=(
            validate_phone_num,
        )
    )


class OrderedItem(models.Model):
    item_id = models.IntegerField()

    item_size = models.CharField(
        max_length=1
    )

    item_quantity = models.IntegerField()

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
