import asyncio
import aiohttp
from bs4 import BeautifulSoup


class N11Scraper:
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
                # price_without_discount = self.extract_price_without_discount(soup)
                review_count = self.extract_review_count(soup)
                rating_count = self.extract_rating_count(soup)
                main_image_url = self.extract_main_image_url(soup)
                all_images = self.extract_all_images(soup)
                self.data.append({'product_name': product_name,
                                  'price': price,

                                  'seller': seller,
                                  'review_count': review_count,
                                  'rating_count': rating_count,
                                  'main_image_url': main_image_url,
                                  'all_images': all_images
                                  })

    def extract_price(self, soup):
        price_tag = soup.find(class_='unf-p-summary-price')
        return price_tag.text.strip() if price_tag else 'Price not found'

    # def extract_price_without_discount(self, soup):
    #     old_price_tag = soup.find('div', id='unf-p-id').find('div', class_='priceContainer').find('del',class_='oldPrice')
    #     return old_price_tag.text.strip() if old_price_tag else 'Discounted Price not found'

    def extract_product_name(self, soup):
        product_name_tag = soup.find(class_='proName')
        return product_name_tag.text.strip() if product_name_tag else 'Product name not found'

    def extract_seller(self, soup):
        seller_tag = soup.find(class_='unf-p-seller-name')
        return seller_tag.text.strip() if seller_tag else 'Seller not found'

    def extract_review_count(self, soup):
        review_count_tag = soup.find(class_='reviewNum')
        return review_count_tag.text.strip() if review_count_tag else 'Review count not found'

    def extract_rating_count(self, soup):
        rating_count_tag = soup.find(class_='ratingScore')  # Doğru sınıf adını kontrol ediniz
        return rating_count_tag.text.strip() if rating_count_tag else 'Rating count not found'

    def extract_main_image_url(self, soup):
        main_image_url_tag = soup.find('img', class_='unf-p-img')
        return main_image_url_tag['data-original'] if main_image_url_tag else 'Main Image Url not found'

    def extract_all_images(self, soup):
        return [image_tag.get('data-full') for image_tag in soup.find_all('div', class_='unf-p-thumbs-item') if
                image_tag.get('data-full')]

