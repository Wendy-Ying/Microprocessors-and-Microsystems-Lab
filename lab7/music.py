import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

def pwm(freq, dur):
    pi_pwm.start(50)
    pi_pwm.ChangeFrequency(freq)
    time.sleep(0.3*dur)
    pi_pwm.stop()
    time.sleep(0.1*dur)

def music(tune):
    for i in range(0, len(tune)):
        pwm(pitch_to_freq[tune[i][0]], tune[i][1])

pitch_to_freq = {
    'C': 261, # Do
    'D': 293, # Re
    'E': 329, # Mi
    'F': 349, # Fa
    'G': 392, # So
    'A': 440, # La
    'B': 493 # Si
}

try:
    pi_pwm = GPIO.PWM(11, 440)
    
    tune = [
        ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
        ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',2),
        ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
        ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
        ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
        ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',2)
    ]
    music(tune)

    GPIO.cleanup()

except KeyboardInterrupt:
    pi_pwm.stop()
    GPIO.cleanup()