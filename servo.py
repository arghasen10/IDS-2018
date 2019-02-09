import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
pwm=GPIO.PWM(18,50)
pwm.start(3.5)
time.sleep(5)
pwm.ChangeDutyCycle(12.5)
time.sleep(1)
pwm.stop()

