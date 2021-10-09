import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.freebuf.com/sectool/289235.html")
bs = BeautifulSoup(r.text, features='html.parser')
l = bs.find(name='span', attrs={"class": "title-span"}).text
print(l)
