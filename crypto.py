import urllib2
import json
from bs4 import BeautifulSoup

url = 'https://bittrex.com/Market/Index?MarketName=BTC-RISE'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

print soup.prettify()


