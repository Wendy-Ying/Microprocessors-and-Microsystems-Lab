import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(12,GPIO.IN)

try:
    while True:
        if GPIO.input(12) == 0:
            GPIO.output(35,True)
            GPIO.output(37,False)
        else:
            GPIO.output(35,False)
            GPIO.output(37,True)
except KeyboardInterrupt:
    GPIO.cleanup()