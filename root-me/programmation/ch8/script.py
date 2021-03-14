import requests
import bs4
from PIL import Image
import base64
import pytesseract

import numpy as np
import io

# L'idée pour le challenge est de récupérer l'image en base64, la processer , et la faire passer en logiciel OCR, ensuite, la réponse est envoyée directement

# nécessaire pour configurer tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# proxy pour observer la request avec Burp
proxies = {
    "http": "http://127.0.0.1:8080"
}

url = 'http://challenge01.root-me.org/programmation/ch8/'

# set cookie de session
c1 = dict(PHPSESSID='my_cookie_session')
r = requests.get(url, cookies=c1)

# parse html to find picture
html = bs4.BeautifulSoup(r.text, features="html.parser")

mImg = html.find('img')
mString = mImg.attrs['src']

# we get the base64
imgString = mString.split('base64,')[1]

# creation of a new image
image_string = io.BytesIO(base64.b64decode(imgString))
image = Image.open(image_string)

# process the image to transform black pixels to white for better precision
data = np.array(image)
rgb = data[:, :, :3]

color = [0, 0, 0]
white = [255, 255, 255]

# masking of black pixels to white
mask = np.all(rgb == color, axis=-1)
data[mask] = white

# creation of new image
new_im = Image.fromarray(data)
# save picture just for debug
new_im.save('out.png')

# this is the answer
answer = pytesseract.image_to_string(new_im)
print('answer is: ' + answer)

# sending request
res = requests.post(url, cookies=c1, data={
                    'cametu': answer.strip()}, proxies=proxies)

# this is the response
print(res.text)
