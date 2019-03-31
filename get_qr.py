import scan
import requests
from PIL import Image
from io import BytesIO

if __name__ == "__main__":
    resp = requests.get('https://hackattic.com/challenges/reading_qr/problem?access_token=bcf0a1b846853da6')
    iurl = resp.json()['image_url']
    image_resp = requests.get(iurl)
    image = Image.open(BytesIO(image_resp.content))
    image.show()
