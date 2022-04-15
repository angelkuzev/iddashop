from django.urls import path
from iddashop.main import views as views

urlpatterns = (
    path('', views.HomePageView.as_view(), name='home'),

    path('item/add', views.CreateItemView.as_view(), name='create item'),
    path('item/view/<int:pk>', views.ItemDetailsView.as_view(), name='item details'),

    path('cart', views.show_cart, name='show cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add to cart'),
    path('remove-from-cart/<int:pk>/<str:size>', views.remove_from_cart, name='remove from cart'),

    path('order/confirm', views.order_confirm_page, name='confirm order'),
    path('orders/', views.ListOrdersView.as_view(), name='list orders'),

)
