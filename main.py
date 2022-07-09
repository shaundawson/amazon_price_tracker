from bs4 import BeautifulSoup
import requests

product_url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

# Scrape Amazon
response = requests.get(product_url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
