import Jetson.GPIO as GPIO
import time

w11 = 11
w12 = 7
w21 = 13
w22 = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(w11, GPIO.OUT)
GPIO.setup(w12, GPIO.OUT)
GPIO.setup(w21, GPIO.OUT)
GPIO.setup(w22, GPIO.OUT)
print("Initialized Done.....")

while True:
	s = input("Enter command for robot")
	print(s)
	if s == 'front':
		print("Moving Forward..")
		GPIO.output(w11, GPIO.HIGH)
		GPIO.output(w12, GPIO.LOW)
		GPIO.output(w21, GPIO.HIGH)
		GPIO.output(w22, GPIO.LOW)
	elif s == 'back':
		print("Moving Backward..")
		GPIO.output(w11, GPIO.LOW)
		GPIO.output(w12, GPIO.HIGH)
		GPIO.output(w21, GPIO.LOW)
		GPIO.output(w22, GPIO.HIGH)
	elif s == 'left':
		print("Turning Left..")
		GPIO.output(w11, GPIO.LOW)
		GPIO.output(w12, GPIO.LOW)
		GPIO.output(w21, GPIO.HIGH)
		GPIO.output(w22, GPIO.LOW)
	elif s == 'right':
		print("Turning Right..")
		GPIO.output(w11, GPIO.HIGH)
		GPIO.output(w12, GPIO.LOW)
		GPIO.output(w21, GPIO.LOW)
		GPIO.output(w22, GPIO.LOW)
	elif s == 'stop':
		print("Stopping")
		GPIO.output(w11, GPIO.LOW)
		GPIO.output(w12, GPIO.LOW)
		GPIO.output(w21, GPIO.LOW)
		GPIO.output(w22, GPIO.LOW)
	else:
		print("Enter the correct command")
	time.sleep(2)
