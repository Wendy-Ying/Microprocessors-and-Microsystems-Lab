import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

def set_angle(angle):
    duty = angle / 9 + 2.5
    pwm.ChangeDutyCycle(duty)
    print(duty)

    
try:
    pwm = GPIO.PWM(11,50)
    pwm.start(2.5)
    last_angle = 0
    while True:
        angle = int(input())
        if angle < last_angle:
            for i in range(last_angle, angle, -1):
                set_angle(i)
                time.sleep(0.01)
        elif angle > last_angle:
            for i in range(last_angle, angle):
                set_angle(i)
                time.sleep(0.01)
        last_angle = angle
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()