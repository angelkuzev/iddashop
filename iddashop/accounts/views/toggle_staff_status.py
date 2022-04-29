from django.shortcuts import redirect
from iddashop.accounts.models import IddashopUser


def toggle_staff_status(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    user = IddashopUser.objects.get(pk=pk)
    user.is_staff = not user.is_staff
    user.save()

    return redirect('show all users')
