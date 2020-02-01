from django.urls import path
from main.views import ListScrapingView

app_web = 'main'

urlpatterns = [
    path('', ListScrapingView.as_view(), name='list-scraping'),
]