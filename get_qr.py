from scan import scan
import requests
import cv2
from io import BytesIO
from PIL import Image
import numpy as np
import json

if __name__ == "__main__":
    # get request for image_url
    resp = requests.get('https://hackattic.com/challenges/reading_qr/problem?access_token=bcf0a1b846853da6')
    iurl = resp.json()['image_url']

    # get request on image url for image in byte form
    image_resp = requests.get(iurl)

    # byte to opencv2 image
    image_pil = Image.open(BytesIO(image_resp.content))
    image_np = np.array(image_pil)
    data = scan(image_np)
    payload = json.dumps({"code": data})
    resp = requests.post('https://hackattic.com/challenges/reading_qr/solve?access_token=bcf0a1b846853da6', data=payload)
    print(resp.json())
