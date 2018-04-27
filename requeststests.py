import requests

params = {"#q": "pizza"}
r = requests.get("http://www.bing.com", params=params)
print("Status", r.status_code)

#print(r.headers)
#print(r.text)
print(r.url)

f = open("./page.html", "w+")
f.write(r.text)