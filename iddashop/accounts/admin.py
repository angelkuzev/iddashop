from django.contrib import admin
from iddashop.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass