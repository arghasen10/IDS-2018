import RPi.GPIO as GPIO
import os
from datetime import datetime
import time

import Email


GPIO.setmode(GPIO.BCM)

# Shooting Video and capturing image from the Pi camera
def picamerause(num):
    string = 'fswebcam -p YUYV -d /dev/video0 -r 640x480 '
    string += 'image'+str(num)+'.jpg'
    os.system(string)
    time.sleep(1)
    


def main():
    # use Raspberry Pi board pin numbers
    # set GPIO Pins
    pinTrigger = 23
    pinEcho = 24
    servo = 18
    # set GPIO input and output channels
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    GPIO.setup(servo,GPIO.OUT)
    num = 0

    while True:
        GPIO.output(pinTrigger, False)
        time.sleep(1)
        # set Trigger to HIGH
        GPIO.output(pinTrigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

        startTime = time.time()
        stopTime = time.time()

        # save start time
        while 0 == GPIO.input(pinEcho):
            startTime = time.time()

        # save time of arrival
        while 1 == GPIO.input(pinEcho):
            stopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print("Distance: %.1f cm" % distance)
        if (distance <= 30):
            num += 1
            print('Capturing video and Photo of Intruder...')
            #TODO 
            picamerause(num)
            print("Sending Mail......")
            Email.sendMail(num)
            print("Waiting for User's command...")
            res = Email.read_email_from_gmail()
            if res:
##                GPIO.output(red, False)
##                GPIO.output(yellow, False)
##                GPIO.output(green, True)
                pwm=GPIO.PWM(18,150)
                pwm.start(20)
                time.sleep(3)
                pwm.ChangeDutyCycle(0.15)
                time.sleep(1)
                pwm.stop()
                print('Open Door')
            else:
                print('Close Door')
            
    GPIO.setwarnings(False)
    GPIO.cleanup()

if __name__=='__main__':
    main()

