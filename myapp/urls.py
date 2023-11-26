from django.urls import path
from .views import ItemListCreateView
from .views import scrape_and_return_json

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
]

urlpatterns = [
    path('scrape/', scrape_and_return_json, name='scrape-and-return-json'),
]