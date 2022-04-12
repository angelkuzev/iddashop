from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.main.models import Item


class HomePageView(views.ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'


class CreateItemView(views.CreateView):
    model = Item
    template_name = 'add_product.html'
    fields = ('picture', 'name', 'description')
    success_url = reverse_lazy('home')


