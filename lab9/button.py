import lirc
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.output(35, False)
GPIO.output(37, False)

def pwm(freq, dur):
    pi_pwm.start(50)
    pi_pwm.ChangeFrequency(freq)
    time.sleep(0.3*dur)
    pi_pwm.stop()
    time.sleep(0.1*dur)

def music(tune):
    pwm(pitch_to_freq[tune[0]], tune[1])

pitch_to_freq = {
    'C': 261, # Do
    'D': 293, # Re
    'E': 329, # Mi
    'F': 349, # Fa
    'G': 392, # So
    'A': 440, # La
    'B': 493 # Si
}

pi_pwm = GPIO.PWM(11, 440)

def pasreset(data):
    if data == 'echo "KEY_1"':
        print("1 Pressed")
        return 1
    elif data == 'echo "KEY_2"':
        print("2 Pressed")
        return 2
    elif data == 'echo "KEY_3"':
        print("3 Pressed")
        return 3
    elif data == 'echo "KEY_4"':
        print("4 Pressed")
        return 4
    elif data == 'echo "KEY_5"':
        print("5 Pressed")
        return 5
    elif data == 'echo "KEY_6"':
        print("6 Pressed")
        return 6
    elif data == 'echo "KEY_7"':
        print("7 Pressed")
        return 7
    elif data == 'echo "KEY_8"':
        print("8 Pressed")
        return 8
    elif data == 'echo "KEY_9"':
        print("9 Pressed")
        return 9

with lirc.LircdConnection("button.py",) as conn:
    while True:
        string = conn.readline()
        key = pasreset(string)
        if key == 1:
            music(['C',1])
        elif key == 2:
            music(['D',1])
        elif key == 3:
            music(['E',1])
        elif key == 4:
            music(['F',1])
        elif key == 5:
            music(['G',1])
        elif key == 6:
            music(['A',1])
        elif key == 7:
            GPIO.output(35, True)
            GPIO.output(37, False)
        elif key == 8:
            GPIO.output(35, False)
            GPIO.output(37, True)
        elif key == 9:
            GPIO.output(35, False)
            GPIO.output(37, False)
