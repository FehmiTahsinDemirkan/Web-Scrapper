import asyncio
import json
from trendyol_scraper import TrendyolScraper
from n11_scraper import N11Scraper
from file_exporter import JSONExporter
import email_sender
from log_module import logger  # Log modülünü ekledik

async def main():
    logger.info("Program baslatıldı.")  # Başlangıç logu

    # Load URLs from config file
    with open('Data/urls.json', 'r') as file:
        urls = json.load(file)

    # Scrape Trendyol product data
    trendyol_scraper = TrendyolScraper(urls['trendyol'])
    await trendyol_scraper.scrape()

    # Check if any Trendyol data is scraped
    if trendyol_scraper.data:
        # Export Trendyol data to JSON file
        trendyol_json_exporter = JSONExporter()
        trendyol_json_exporter.export_data(trendyol_scraper.data, 'Trendyoldata.json')
        logger.info("Trendyol verileri basarıyla çekildi ve JSON dosyasına aktarıldı.")

    # Scrape Hepsiburada product data
    hepsiburada_scraper = N11Scraper(urls['n11'])
    await hepsiburada_scraper.scrape()

    # Check if any Hepsiburada data is scraped
    if hepsiburada_scraper.data:
        # Export Hepsiburada data to JSON file
        hepsiburada_json_exporter = JSONExporter()
        hepsiburada_json_exporter.export_data(hepsiburada_scraper.data, 'n11.json')
        logger.info("N11 verileri başarıyla çekildi ve JSON dosyasına aktarıldı.")

    logger.info("Program sonlandırıldı.")  # Bitiş logu

asyncio.run(main())
