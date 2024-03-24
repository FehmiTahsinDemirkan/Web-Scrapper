import requests

response = requests.get('https://www.hepsiburada.com/')
if response.status_code == 200:
    print("Hepsiburada web sitesine erişebiliyorsunuz.")
else:
    print("Hepsiburada web sitesine erişilemedi. Hata kodu:", response.status_code)
