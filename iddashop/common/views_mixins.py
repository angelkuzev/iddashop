from django.shortcuts import redirect


class LoginRegisterRedirect:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class NotAuthRedirect:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class NotStaffRedirect:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class NotAdminRedirect:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

