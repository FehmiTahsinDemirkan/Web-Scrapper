import requests

response = requests.get('https://www.amazon.com.tr/')
if response.status_code == 400:
    print(" web sitesine erişebiliyorsunuz.")
else:
    print(" web sitesine erişilemedi. Hata kodu:", response.status_code)
