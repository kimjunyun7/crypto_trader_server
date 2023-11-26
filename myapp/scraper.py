# myapp/scraper.py
import requests
from bs4 import BeautifulSoup

class ExchangeInfoScraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape_data(self):
        # Send a GET request to the URL
        response = requests.get(self.url)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Select elements using CSS selectors
            english_names = [element.text.strip() for element in soup.select('a > div > div > p')]
            currencies = [element.text.strip() for element in soup.select('div > a.sc-cefb3d9b-0.iTwyIj.cmc-link')]

            # Create a list of dictionaries with 'englishName' and 'currency'
            self.data = [{'englishName': english_name, 'currency': currency} for english_name, currency in zip(english_names, currencies)]
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    def to_json(self):
        return self.data
