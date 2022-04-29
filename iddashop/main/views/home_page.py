from django.views import generic as views
from iddashop.main.models import Item, Category


class HomePageView(views.ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        men_categories = Category.objects.filter(gender=Category.MALE)
        women_categories = Category.objects.filter(gender=Category.FEMALE)

        gender = self.request.GET.get('gender')
        category = self.request.GET.get('category')

        if gender:
            context['gender'] = gender
            context['items'] = [item for item in context['items'] if item.category.gender == gender]
            context['categories'] = men_categories if gender == 'Male' else women_categories

        if category:
            context['category_name'] = category
            context['items'] = [item for item in context['items'] if item.category.name == category]


        return context
