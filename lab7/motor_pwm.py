import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

def set_angle(angle):
    duty = angle / 9 + 2.5
    pwm.ChangeDutyCycle(duty)
    
try:
    pwm = GPIO.PWM(11,50)
    pwm.start(2.5)
    while True:
        for i in range(0, 180):
            set_angle(i)
            time.sleep(0.01)
    pwm.stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()