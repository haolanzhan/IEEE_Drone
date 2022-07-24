import requests
from picamera import PiCamera
from time import sleep
import serial
import random

#ser = serial.Serial('/dev/ttyACM0',9600)
ser = serial.Serial('/dev/ttyS0',9600)
ser.flush()

camera = PiCamera()

print("Welcome to our mask-wearing object detection program!")
print("Waiting to receive message from ESP32")

j = int(0)
test = 1
test2 = 0

#infinite loop
while True:
	if ser.inWaiting() > 0:
		print("data received")

		data = ser.read()

		print(data)
		
		if data == test.to_bytes(1, byteorder='big'):

			print("About to take a picture!")
			#take a picture and save it
			camera.capture('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j)

			print("Picture taken ... running Nanonets API ...")

            		#Call's the nanonets API based on a given input image 
			url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

			data = {'file': open('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j, 'rb'), 'modelId': ('', 'b3cb3905-6eff-4c0c-815b-83fb5e0a286c')}

			response = requests.post(url, auth= requests.auth.HTTPBasicAuth('LoKbe6mEh4pgyEqTxVJmpaUiMG3_9dAs', ''), files=data)

			print(response.text)

            		#Organizes output and print 
			x=response.json()
			#ser.println(x["message"])
			if x["message"]=="Success":
				print("Wow, the image has been successfully classified! Technology is insane :)")
				print()
				for i in x["result"][0]["prediction"]:
					print("Label : {}         Probability : {}".format(i["label"],i["probability"]))
					print("____________________________________________________")
				print("\nOur final prediction is= {}".format(x["result"][0]["prediction"][0]["label"]))
			else:
				print("Oh dear. The model could not classify the given image. Sorry!")

			j += 1
			print("Looping...")

		elif data == test2.to_bytes(1, byteorder='big'):
			 break

#End of program
print("Finished!")
