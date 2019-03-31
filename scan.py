import numpy as np
import cv2

def scan(image):
    qrDecoder = cv2.QRCodeDetector()
    data, bbox, newImage = qrDecoder.detectAndDecode(image)
    if len(data) > 0:
        return data
    else:
        print("No QR Code detected")
