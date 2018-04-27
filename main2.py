import requests
from io import BytesIO
from PIL import Image

#r = requests.get("https://wallpaper.wiki/wp-content/uploads/2017/04/wallpaper.wiki-Epic-Star-Wars-Backgrounds-Free-Download-PIC-WPB006362.jpg")

r = requests.get("https://img00.deviantart.net/d61e/i/2013/058/e/5/dead_space_3___wallpaper_hd_1080p_by_rikoray-d5wdnan.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("cannot save image.")