import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'


calling = dict()
calling['address'] = input('Enter location: ')
calling['key'] = "42"

url = serviceurl + urllib.parse.urlencode(calling)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

place_id = js['results'][0]['place_id']

print('Place id' , place_id)