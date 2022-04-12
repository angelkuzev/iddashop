from django.core.validators import MinLengthValidator
from django.db import models


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
