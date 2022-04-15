from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.common.helpers import get_user_phone_num, get_user_address
from iddashop.main.forms import CreateItemForm
from iddashop.main.models import Item, Quantity, Order, OrderedItem


class HomePageView(views.ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'


class CreateItemView(views.CreateView):
    form_class = CreateItemForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('home')


class ItemDetailsView(views.DetailView):
    model = Item
    template_name = 'view_item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantities'] = Quantity.objects.get(pk=context['item'].id)
        return context


def add_to_cart(request, pk):
    size = request.POST['group1']
    item_db = Item.objects.get(pk=pk)

    item = {
        'pk': pk,
        'size': size,
        'title': item_db.name,
        'image_url': item_db.picture.url,
        'quantity': 1,
        'price_per_item': item_db.price,
    }

    if 'cart' not in request.session:
        request.session['cart'] = [item]
    else:
        items = request.session['cart']

        exist = next((item for item in items if item['pk'] == pk and item['size'] == size), None)
        if exist:
            exist['quantity'] += 1
        else:
            items.append(item)
        request.session['cart'] = items

    return redirect('show cart')


def show_cart(request):
    context = {
        'items': None,
    }

    if 'cart' not in request.session:
        return render(request, 'cart.html', context)

    context['items'] = request.session['cart']
    return render(request, 'cart.html', context)


def remove_from_cart(request, pk, size):
    cart = request.session['cart']
    cart = list(filter(lambda i: i['pk'] != pk or i['size'] != size, cart))
    request.session['cart'] = cart

    return redirect('show cart')


def order_confirm_page(request):
    user = request.user
    phone = get_user_phone_num(user.id)
    address = get_user_address(user.id)
    context = {
        'phone_num': phone,
        'address': address,
        'cart': request.session['cart'],
    }

    if request.method == "POST":
        order = Order(ordered_by=user, client_address=get_user_address(user.id),
                      client_phone_num=get_user_phone_num(user.id), )
        order.save()

        for item in request.session['cart']:
            ordered_item = OrderedItem(item_id=item['pk'],
                                       item_size=item['size'],
                                       item_quantity=item['quantity'],
                                       order=order
                                       )
            ordered_item.save()

        request.session['cart'] = []

        return redirect('home')

    return render(request, 'order_confirm.html', context)


class ListOrdersView(views.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
