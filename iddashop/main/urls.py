from django.urls import path
from iddashop.main.views.home_page import HomePageView
from iddashop.main.views import item_views
from iddashop.main.views import cart_views
from iddashop.main.views import order_views

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),

    path('item/add', item_views.CreateItemView.as_view(), name='create item'),
    path('item/view/<int:pk>', item_views.ItemDetailsView.as_view(), name='item details'),
    path('categories/add', item_views.AddCategoryView.as_view(), name='add category'),

    path('cart', cart_views.show_cart, name='show cart'),
    path('add-to-cart/<int:pk>', cart_views.add_to_cart, name='add to cart'),
    path('remove-from-cart/<int:pk>/<str:size>', cart_views.remove_from_cart, name='remove from cart'),

    path('order/confirm', order_views.order_confirm_page, name='confirm order'),
    path('orders/', order_views.ListOrdersView.as_view(), name='list orders'),
    path('orders/<int:pk>', order_views.OrderDetailsView.as_view(), name='order details'),
    path('orders/manage', order_views.ManageOrdersView.as_view(), name='manage orders'),
    path('orders/accept/<int:pk>', order_views.AcceptOrderView.as_view(), name='accept order'),

)
