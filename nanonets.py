import requests

from picamera import PiCamera
from time import sleep

camera = PiCamera()

print("Welcome to our mask-wearing object detection program!")
print("To take a picture and evaluate under the model, enter 1")
print("To exit, enter 0")

loop = input("Please enter 0 or 1:\n")
loop = int(loop)
j = int(0)

while loop != 0:
	#break if given an invalid input
	if (loop != 1):
		break

	#take a picture and save it 
	sleep(5)
	camera.capture('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j)

	
	#Call's the nanonets API based on a given input image 
	url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

	data = {'file': open('/home/pi/IEEE/pictures/evaluate_image%s.jpg' % j, 'rb'), 'modelId': ('', 'b3cb3905-6eff-4c0c-815b-83fb5e0a286c')}

	response = requests.post(url, auth= requests.auth.HTTPBasicAuth('LoKbe6mEh4pgyEqTxVJmpaUiMG3_9dAs', ''), files=data)

	print(response.text)

	#This organizes the output of the nanonets API call
	x=response.json()
	if x["message"]=="Success":
		print("Wow, the image has been successfully classified! Technology is insane :)")
		print()
		for i in x["result"][0]["prediction"]:
			print("Label : {}         Probability : {}".format(i["label"],i["probability"]))
			print("____________________________________________________")
		print("\nOur final prediction is= {}".format(x["result"][0]["prediction"][0]["label"]))
	else:
		print("Oh dear. The model could not classify the given image. Sorry!")

	
	#take another photo
	j +=  1
	print()
	print("Do you want to evaluate another photo? Same instructions as before")

	loop = input("Please enter 0 or 1:\n")
	loop = int(loop)
#End of program
print("Finished!")
