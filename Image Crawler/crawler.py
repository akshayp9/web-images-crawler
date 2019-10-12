from bs4 import *
import requests as rq
import os

req = rq.get("https://www.pexels.com/search/programming/")

soup2 = BeautifulSoup(req.text, 'html.parser')

links = []

x = soup2.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
    links.append(img['src'])

# for l in links:
#     print(l)

os.mkdir('photos')
i = 1

for index, img_link in enumerate(links):
    if i<=10:
        img_data = rq.get(img_link).content
        with open("photos/" + str(index + 1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break    