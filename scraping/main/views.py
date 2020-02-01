from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import Scraping

class ListScrapingView(ListView):
    model = Scraping
    paginate_by = 10
    context_object_name = 'scrapings'
