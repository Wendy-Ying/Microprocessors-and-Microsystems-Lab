import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.IN)
GPIO.setwarnings(False)

try:
    while True:
        d_list = []
        for _ in range(1,100):
            GPIO.output(38,True)
            time.sleep(1e-5)
            GPIO.output(38,False)
            while True:
                if GPIO.input(40) == 1:
                    break
            t1 = time.time()
            while True:
                if GPIO.input(40) == 0:
                    break
            t2 = time.time()
            d = (t2-t1) * 343 /2
            d_list.append(d)
        d_list = np.array(d_list)
        print(f"distance: {d_list.mean()} m")
except KeyboardInterrupt:
    GPIO.cleanup()