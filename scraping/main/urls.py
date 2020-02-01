from django.urls import path
from main.views import (ListScrapingView, SearchScrapingView,)

app_name = 'main'

urlpatterns = [
    path('', ListScrapingView.as_view(), name='list-scraping'),
    path('search/', SearchScrapingView.as_view(), name='search-scraping'),
]