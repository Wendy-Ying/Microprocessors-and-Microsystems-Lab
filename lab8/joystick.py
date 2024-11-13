import smbus
import time
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

try:
    pi_pwm = GPIO.PWM(11, 100)
    pi_pwm.stop()
    
    while True:
        data0 = bus.read_byte_data(0x48, 0x40)
        data1 = bus.read_byte_data(0x48, 0x41)
        data2 = bus.read_byte_data(0x48, 0x42)
        print(data0, data1, data2)

        bus.write_byte_data(0x48, 0x42, int(255-data2))
        if data1 == 0:
            pi_pwm.start(50)
        else:
            pi_pwm.stop()
            
    
except KeyboardInterrupt:
    bus.close()
    pi_pwm.stop()
    GPIO.cleanup()