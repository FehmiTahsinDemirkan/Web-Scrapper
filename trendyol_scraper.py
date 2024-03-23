import aiohttp
from bs4 import BeautifulSoup
import asyncio

class ProductScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = []

    async def fetch_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.text()
                    return data

    async def scrape(self):
        tasks = [self.fetch_data(url) for url in self.urls]
        results = await asyncio.gather(*tasks)
        for html_content in results:
            soup = BeautifulSoup(html_content, 'html.parser')
            price_tag = soup.find(class_='prc-dsc')
            if price_tag:
                price = price_tag.text.strip()
                self.data.append(price)
            else:
                self.data.append('Price not found')
