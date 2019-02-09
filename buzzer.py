import RPi.GPIO as GPIO
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 13
GPIO.setup(buzzer,GPIO.OUT)
#GPIO.output(buzzer,GPIO.HIGH)
p = GPIO.PWM(12,50)
p.start(0)
try:
	while 1:
		for dc in range(0,101,5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100,-1,-5):
			
print("Beep")
sleep(10)
GPIO.output(buzzer,GPIO.LOW)
print("No Beep")
sleep(1)
