from django.shortcuts import render, redirect


def show_cart(request):
    if not request.user:
        return redirect('home')

    context = {
        'items': None,
    }

    if 'cart' in request.session:
        context['items'] = request.session['cart']

    return render(request, 'items/cart.html', context)