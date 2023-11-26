from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from .models import Item, ScrapedData
from .serializers import ItemSerializer


from .scraper import ExchangeInfoScraper

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def scrape_and_return_json(request):
    url = 'https://coinmarketcap.com/ko/exchanges/upbit/?type=spot'
    scraper = ExchangeInfoScraper(url)
    scraper.scrape_data()
    result_json = scraper.to_json()

    # Store the scraped data in the ScrapedData model
    for data in result_json:
        ScrapedData.objects.create(english_name=data['englishName'], currency=data['currency'])

    return JsonResponse(result_json, safe=False)