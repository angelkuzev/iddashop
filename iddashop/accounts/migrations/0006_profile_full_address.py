# Generated by Django 4.0.4 on 2022-04-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_delete_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_address',
            field=models.CharField(default='Plovdiv ul. Akula 8', max_length=256),
            preserve_default=False,
        ),
    ]