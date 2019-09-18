from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(), "html.parser")

print("h1: ", bs0bj.h1)
# <h1>An Interesting Title</h1>

