import asyncio
import json
import os

from trendyol_scraper import TrendyolScraper
from n11_scraper import N11Scraper
from file_exporter import JSONExporter
from email_sender import EmailSender
from log_module import logger

async def main():
    logger.info("Program başlatıldı.")  # Başlangıç logu

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
        logger.info("Trendyol verileri başarıyla çekildi ve JSON dosyasına aktarıldı.")

    # Scrape Hepsiburada product data
    hepsiburada_scraper = N11Scraper(urls['n11'])
    await hepsiburada_scraper.scrape()

    # Check if any Hepsiburada data is scraped
    if hepsiburada_scraper.data:
        # Export Hepsiburada data to JSON file
        hepsiburada_json_exporter = JSONExporter()
        hepsiburada_json_exporter.export_data(hepsiburada_scraper.data, 'n11.json')
        logger.info("N11 verileri başarıyla çekildi ve JSON dosyasına aktarıldı.")

    # Send email with attachments
    email_sender_instance = EmailSender(
        sender_email=os.getenv("SENDER_EMAIL"),
        sender_password=os.getenv("SENDER_PASSWORD")
    )

    await email_sender_instance.send_email(
        recipient_email="fehmitahsindemirkan@gmail.com",
        subject="Scraping Results",
        message="Attached are the scraping results.",
        attachments=["Exported Files/Trendyoldata.json", "Exported Files/n11.json"]
    )

    logger.info("E-posta gönderildi.")  # Log

    logger.info("Program sonlandırıldı.")  # Bitiş logu

asyncio.run(main())
