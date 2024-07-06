import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
page = (urllib.request.urlopen(url)).read()
print('Retrieved', len(page), 'characters')

info = json.loads(page)
print('Count:', len(info["comments"]))

total = 0

for item in info["comments"]:
    total = total + int(item["count"])

print('Sum:', total)