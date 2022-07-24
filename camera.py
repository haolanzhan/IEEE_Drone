from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range(5):

	sleep(5)
	camera.capture('/home/pi/IEEE/pictures/new2_image%s.jpg' % i)

