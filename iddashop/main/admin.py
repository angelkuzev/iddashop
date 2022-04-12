from django.contrib import admin
from iddashop.main.models import Item


@admin.register(Item)
class ProfileAdmin(admin.ModelAdmin):
    pass