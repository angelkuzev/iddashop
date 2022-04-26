from django.contrib import admin
from iddashop.accounts.models import Profile, IddashopUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(IddashopUser)
class IddashopUserAdmin(admin.ModelAdmin):
    pass