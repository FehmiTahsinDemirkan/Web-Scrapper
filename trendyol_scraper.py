import aiohttp
from bs4 import BeautifulSoup
import asyncio


class TrendyolScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = []

    async def fetch_data(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                return None

    async def scrape(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_data(session, url) for url in self.urls]
            results = await asyncio.gather(*tasks)

        for html_content in results:
            soup = BeautifulSoup(html_content, 'html.parser')
            price = self.extract_price(soup)
            seller = self.extract_seller(soup)
            product_name = self.extract_product_name(soup)
            price_without_discount = self.extract_price_without_discount(soup)
            review_count = self.extract_review_count(soup)
            self.data.append({'product_name': product_name,
                              'seller': seller,
                              'price': price,
                              'price_without_discount': price_without_discount,
                              'review_count': review_count
                              })

    def extract_price(self, soup):
        price_tag = soup.find(class_='prc-dsc')
        return price_tag.text.strip() if price_tag else 'Price not found'

    def extract_price_without_discount(self, soup):
        price_tag = soup.find(class_='prc-org')
        return price_tag.text.strip() if price_tag else 'Discounted Price not found'

    def extract_product_name(self, soup):
        product_name_tag = soup.find(class_='pr-new-br')
        return product_name_tag.find('span').text.strip() if product_name_tag else 'Product name not found'

    def extract_seller(self, soup):
        seller_tag = soup.find(class_='product-brand-name-with-link') or soup.find(
            class_='product-brand-name-without-link')
        return seller_tag.text.strip() if seller_tag else 'Seller not found'

    def extract_review_count(self, soup):
        a_tag = soup.find("a", class_='rvw-cnt-tx')
        if a_tag:
            review_count_tag = a_tag.find(class_='total-review-count')
            if review_count_tag:
                return review_count_tag.text.strip()
        return 'Review count not found'

