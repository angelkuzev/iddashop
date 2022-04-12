from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters!')


def validate_phone_num(value):
    if not len(value) == 10:
        raise ValidationError('Phone number must be 10 digits long!')

    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits!')

    if not value[0] == '0':
        raise ValidationError('Phone number must start with 0!')
