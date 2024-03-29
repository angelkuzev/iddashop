from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from iddashop.accounts import views as views

urlpatterns = (
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('register/', views.UserRegisterView.as_view(), name='register user'),
    path('edit/profile/<int:pk>', views.EditProfileView.as_view(), name='edit profile'),
    path('edit/password/', views.ChangeUserPasswordView.as_view(), name='change password'),
    path('password-change-done/', RedirectView.as_view(url=reverse_lazy('home')),
         name='password_change_done'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('login user')), name='logout'),

    path('profile/<int:pk>', views.UserDetailsView.as_view(), name='show profile'),
    path('users/list', views.ManageUsersView.as_view(), name='show all users'),
    path('users/staff/toggle/<int:pk>', views.toggle_staff_status, name='toggle staff status'),
)
