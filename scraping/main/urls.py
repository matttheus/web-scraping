from django.urls import path
from main.views import IndexView

app_web = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]