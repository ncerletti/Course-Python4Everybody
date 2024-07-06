from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = int(input('Enter count - '))
position = int(input('Enter position -'))
count = count + 1

while count > 0:
    print ("retrieving: {0}".format(url))
    page= urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    tag = soup('a')
    url = tag[position-1]['href']
    count = count - 1
