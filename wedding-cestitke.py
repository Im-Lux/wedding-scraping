from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

quote = soup.findAll("p", attrs={"class": "quoteContent"})

for quotes in quote:
    print quotes.text