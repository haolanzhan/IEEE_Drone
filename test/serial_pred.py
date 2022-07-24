import requests
from picamera import PiCamera
from time import sleep
import serial
import random

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()

while True:
    if ser.inWaiting() > 0:

        data = ser.read()
        if data == 1:
            #take a picture and save it 
            camera.capture('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j)

            #Call's the nanonets API based on a given input image 
            url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

            data = {'file': open('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j, 'rb'), 'modelId': ('', 'b3cb3905-6eff-4c0c-815b-83fb5e0a286c')}

            response = requests.post(url, auth= requests.auth.HTTPBasicAuth('LoKbe6mEh4pgyEqTxVJmpaUiMG3_9dAs', ''), files=data)

            print(response.text)

            # send to esp32
            x=response.json()
            ser.println(x["message"])
            if x["message"]=="Success":
                ser.write(2)
            else:
                ser.write(3)
        else:
            ser.write(4)
