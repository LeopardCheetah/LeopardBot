
import json
import requests 
from cachecontrol import CacheControl



link = 'https://lichess.org'

def getRequest(r):
    response = session.get(link + r)
    return response.text


f = open("secrets.txt", "r") 
key = f.readline().strip()

session = CacheControl(requests.Session())
session.headers.update({'Authorization': 'Bearer '+key})





#-------------------------------------------
# woo this works
r = session.get(link + '/api/stream/event', stream = True)
for line in r.iter_lines():
    if line:
        print(line)