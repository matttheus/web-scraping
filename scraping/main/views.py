from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import Scraping

class ListScrapingView(ListView):
    model = Scraping
    context_object_name = 'scrapings'
