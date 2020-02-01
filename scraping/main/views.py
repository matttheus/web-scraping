from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import Scraping


class ListScrapingView(ListView):
    model = Scraping
    paginate_by = 10
    context_object_name = 'scrapings'


class SearchScrapingView(ListView):
    model = Scraping
    paginate_by = 10
    context_object_name = 'scrapings'

    def get_queryset(self):
        query = self.request.GET.get('search')
        scrapings = Scraping.objects.filter(title__contains=query)
        return scrapings
