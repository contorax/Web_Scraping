from bs4 import BeautifulSoup
import requests

res = requests.get  ('http://quotes.toscrape.com/')
soup = BeautifulSoup (res.text, 'lxml')

quote = soup.find_all ('div', {'class': 'quote'})

for q in quote:
	message = q.find ('span', {'class': 'text'})
	# mes = message.decode("windows-1252")
	print (message.text)

	avtor = q.find ('small')
	print ("*** " + avtor.text + " ***")
	# print (avtor.text.encode('utf-8'))
	print ()
	



