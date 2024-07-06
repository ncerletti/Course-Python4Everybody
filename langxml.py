import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
page = (urllib.request.urlopen(url)).read()
print('Retrieved', len(page), 'characters')

tree = ET.fromstring(page)

counts = tree.findall('.//count')
print('Count:', len(counts))

lst = tree.findall('comments/comment')
total = 0 

for comment in lst:
    number = comment.find('count').text
    total = total + int(number)

print('Sum:', total)





