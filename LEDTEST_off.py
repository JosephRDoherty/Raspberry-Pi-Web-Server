

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

GPIO.output(11, GPIO.LOW)

