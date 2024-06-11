from urllib import request
import requests 
import sys 
import json

if len(sys.argv) !=2:
  sys.exit()

response = requests.get('https://itunes.apple.com/search?/entity=song&limit=20&term=' + sys.argv[1])

m = response.json()

for result in m ['results']:
  print(result['trackName'])