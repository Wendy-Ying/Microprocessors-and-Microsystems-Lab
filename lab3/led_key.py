import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

global count
count = 0
GPIO.output(35, False)
GPIO.output(37, False)

def check_input():
    global count
    # 按键检测&消抖
    if GPIO.input(12) == 0:
        time.sleep(0.1)
        if GPIO.input(12) == 0:
            while GPIO.input(12) == 0:
                time.sleep(0.001)
            count += 1
        print(count)
        if count == 5:
            count = 0

def react():
    global count
    while True:
        # 状态响应
        if count == 1:
            GPIO.output(35, False)
            GPIO.output(37, True)
        elif count == 2:
            GPIO.output(35, False)
            GPIO.output(37, True)
            time.sleep(0.5)
            GPIO.output(37, False)
            time.sleep(0.5)
        elif count == 3:
            GPIO.output(37, False)
            GPIO.output(35, True)
        elif count == 4:
            GPIO.output(37, False)
            GPIO.output(35, True)
            time.sleep(0.5)
            GPIO.output(35, False)
            time.sleep(0.5)

try:
    threading.Thread(target=react).start()
    while True:
        check_input()
except KeyboardInterrupt:
    GPIO.cleanup()
