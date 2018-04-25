import requests
r = requests.get("http://google.com")
print("Status", r.status_code)

print(r.headers)
print(r.text)

f = open("./page.html", "w+")
f.write(r.text)