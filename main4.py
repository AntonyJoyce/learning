import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longURL": "http://example.com" }

r = requests.post(url, json=payload)

#f = open("myfile.html", "w+")
#f.write(r.text)

