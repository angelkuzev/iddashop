from iddashop.accounts.models import Profile


def get_user_address(pk):
    profile = Profile.objects.get(pk=pk)
    return profile.full_address


def get_user_phone_num(pk):
    profile = Profile.objects.get(pk=pk)
    return profile.phone_num
