from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from iddashop.accounts.models import IddashopUser
from iddashop.common.validators import validate_phone_num


class Category(models.Model):
    NAME_MAX_LENGTH = 20
    NAME_MIN_LENGTH = 1

    MALE = 'Male'
    FEMALE = 'Female'

    GENDERS = [(x, x) for x in (MALE, FEMALE)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
    )

    def __str__(self):
        return f'{self.gender} {self.name}'


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

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
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
        on_delete=models.PROTECT,
        related_name='ordered_by',
    )

    ordered_on = models.DateTimeField(
        auto_now_add=True,
    )

    accepted_by = models.ForeignKey(
        IddashopUser,
        on_delete=models.CASCADE,
        related_name='accepted_by',
        null=True,
        blank=True,
    )
    accepted_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    expected_arrival = models.DateField(
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
    ITEM_SIZE_MAX_LENGTH = 1

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    item_size = models.CharField(
        max_length=ITEM_SIZE_MAX_LENGTH
    )

    item_quantity = models.IntegerField()

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
