import logging

# Log dosyası adı ve formatı
log_file = 'Logs/crawler.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

# Logger oluşturma ve yapılandırma
logging.basicConfig(filename=log_file, format=log_format, level=logging.INFO)
logger = logging.getLogger()
