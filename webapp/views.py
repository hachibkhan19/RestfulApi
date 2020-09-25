

from .models import Quote, QuoteCategory
from django.views.generic import TemplateView
from django.views.generic import ListView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Hachib khan'
        context['country'] = 'Bangladesh'
        context['list'] = [1, 2, 3, 4, 5]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class QuotesView(ListView):
    template_name = 'quote.html'
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('quote_category')

