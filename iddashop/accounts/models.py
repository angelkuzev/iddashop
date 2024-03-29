from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models
from iddashop.accounts.managers import IddashopUserManager
from iddashop.common.validators import validate_only_letters, validate_phone_num


class IddashopUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = IddashopUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    PHONE_NUM_LENGTH = 10

    profile_picture = models.ImageField(
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    phone_num = models.CharField(
        max_length=PHONE_NUM_LENGTH,
        validators=(
            validate_phone_num,
        )
    )

    full_address = models.CharField(
        max_length=256,
    )

    user = models.OneToOneField(
        IddashopUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'