from bs4 import BeautifulSoup
import lxml
import requests
from config import password, my_email, recipient_address
import smtplib

product_url="https://www.amazon.com/2022-Apple-10-9-inch-Wi-Fi-256GB/dp/B09V3H8MJT/ref=sr_1_1_sspa?crid=2R5GUBO50N8M3&keywords=ipad&qid=1657335976&s=electronics&sprefix=ipad%2Celectronics%2C77&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMjZBOEFMVDVDODEmZW5jcnlwdGVkSWQ9QTA1NTU3ODAyMVhXMkhOTkJBUEI3JmVuY3J5cHRlZEFkSWQ9QTAxMzUzMzYyWjNQQUNRWFNGQ1FPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

# Scrape Amazon
response = requests.get(product_url,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
product_name = soup.title
product_title = soup.find(name="span", id="productTitle").getText().strip()
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_decimal = soup.find(name="span", class_="a-price-fraction").getText()
price_concat = price_whole + price_decimal
price = float(price_concat)
# print(price)
# print(product_title)

if price < 800:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        # connection.starttls()
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=recipient_address, 
            msg=f"Subject:Amazon Price Alert!\n\n{product_title}is now {price}!"
        )
