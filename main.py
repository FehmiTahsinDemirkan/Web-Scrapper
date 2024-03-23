import asyncio
import trendyol_scraper
import file_exporter
import email_sender
import json


async def main():
    with open('Data/trendyolUrls.json', 'r') as file:
        urls = json.load(file)

    if urls:
        # Scrape product data
        scraper = trendyol_scraper.ProductScraper(urls)
        await scraper.scrape()

        # Export data to JSON and CSV files
        json_exporter = file_exporter.JSONExporter()
        csv_exporter = file_exporter.CSVExporter()
        json_exporter.export_data(scraper.data, 'data.json')
        csv_exporter.export_data(scraper.data, 'data.csv')

    #     # Send email with data attached
    #     emailer = email_sender.EmailSender()
    #     await emailer.send_email('recipient@example.com', 'sender@example.com', 'password', 'Product Data',
    #                              'Attached please find the collected data.', scraper.data)
    # else:
    #     print("No URLs found in the JSON file.")


asyncio.run(main())
