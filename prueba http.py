from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

comments = list()

tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    comments.append(num)

print('Count',len(tags))
print('Sum',sum(comments))
