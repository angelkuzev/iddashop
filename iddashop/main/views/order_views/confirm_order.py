from django.shortcuts import render, redirect
from iddashop.common.helpers import get_user_phone_num, get_user_address
from iddashop.main.models import Item, Order, OrderedItem


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
            ordered_item = OrderedItem(item=Item.objects.get(pk=item['pk']),
                                       item_size=item['size'],
                                       item_quantity=item['quantity'],
                                       order=order
                                       )
            ordered_item.save()

        request.session['cart'] = []

        return redirect('home')

    return render(request, 'orders/order_confirm.html', context)
