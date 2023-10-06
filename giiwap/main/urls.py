from django.urls import path
from django.urls.resolvers import URLPattern
from main import views
from .views import IndexView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]