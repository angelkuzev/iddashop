# Generated by Django 4.0.4 on 2022-04-15 11:33

from django.db import migrations, models
import iddashop.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_ordereditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_address',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='client_phone_num',
            field=models.CharField(default=1, max_length=10, validators=[iddashop.common.validators.validate_phone_num]),
            preserve_default=False,
        ),
    ]
