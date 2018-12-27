from bs4 import BeautifulSoup
import requests

res = requests.get  ('http://quotes.toscrape.com/')

print(res)