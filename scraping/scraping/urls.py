from django.urls import path, include

urlpatterns = [
    path('scraping/', include('main.urls')),
]
