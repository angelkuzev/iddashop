from django.urls import path
from iddashop.main import views as views

urlpatterns = (
    path('', views.HomePageView.as_view(), name='home'),
    path('add-item/', views.CreateItemView.as_view(), name='create item'),
)