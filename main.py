from bs4 import BeautifulSoup
import requests
from notification_manager import NotificationManager

TARGET_PRICE = 30.00
product_url = "https://www.amazon.com/-/es/Antonio-Mele-ebook/dp/B09YS5NHX9/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1668871003&sr=8-1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept-Language": "es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3"
}

response = requests.get(url=product_url, headers=headers)
product = response.text

soup = BeautifulSoup(product, "html.parser")
sender = NotificationManager()

product_price = float(soup.select_one("#kindle-price").getText().split("US$")[1])
product_title = soup.select_one("#productTitle").getText()

if product_price < TARGET_PRICE:
    message = f"{product_title} está a: ${product_price}"
    sender.send_emails(message, product_url)

