import requests

my_data = {"name": "Antony", "email": "antonyjoyce@example.co.uk"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)

