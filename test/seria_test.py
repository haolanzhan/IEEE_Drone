
import serial
import random

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()

while True:
    keyin = raw_input('wasd,halt,land,pause \n')

	if keyin == 'r':
		# prediction code goes here

    if keyin == 'p':
        ser.write(b'5')
    elif keyin == 'h':
        ser.write(b'6')
    elif keyin == 'l':
        ser.write(b'7')
    elif keyin == 'w':
        ser.write(b'1')
    elif keyin == 'a':
        ser.write(b'2')
    elif keyin == 's':
        ser.write(b'3')
    elif keyin == 'd':
        ser.write(b'4')
    else:
        ser.write(b'6')

    print('send to Arduino')
    line = ser.readline()
    print('received')
    print(line)
    ser.flush()

"""
import picamera, json, requests, os, random
from time import sleep
from PIL import Image, ImageDraw

#capture an image
camera = picamera.PiCamera()
camera.capture('image1.jpg')
print('caputred image')

#make a prediction on the image
url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
data = {'file': open('REPLACE_IMAGE_PATH.jpg', 'rb'), 'modelId': ('', 'b3cb3905-6eff-4c0c-815b-83fb5e0a286c')}
response = requests.post(url, auth= requests.auth.HTTPBasicAuth('LoKbe6mEh4pgyEqTxVJmpaUiMG3_9dAs', ''), files=data)
print(response.text)
"""