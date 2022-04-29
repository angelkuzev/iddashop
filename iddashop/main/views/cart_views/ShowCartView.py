from django.shortcuts import render


def show_cart(request):
    context = {
        'items': None,
    }

    if 'cart' in request.session:
        context['items'] = request.session['cart']

    return render(request, 'cart.html', context)