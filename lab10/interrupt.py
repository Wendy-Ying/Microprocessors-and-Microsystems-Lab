import RPi.GPIO as GPIO
import time
import threading

LED_RED = 37
LED_GREEN = 35
BUTTON = 12

state = 0
stop_blinking = threading.Event()

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def control_leds():
    while True:
        if state == 0:
            stop_blinking.clear()
        while not stop_blinking.is_set():
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.LOW)
            time.sleep(0.5)
        time.sleep(0.01)

def button_interrupt():
    global state
    while True:
        GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
        time.sleep(0.01)
        if GPIO.input(BUTTON) == 0:
            stop_blinking.set()
            state = (state + 1) % 2
            
def interrupt_callback():
    GPIO.output(LED_RED, GPIO.HIGH)
    GPIO.output(LED_GREEN, GPIO.LOW)
    time.sleep(0.1)
    print("interrupt triggered")
            
def cleanup_gpio():
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.cleanup()

def main():
    setup_gpio()
    led_thread = threading.Thread(target=control_leds)
    button_thread = threading.Thread(target=button_interrupt)
    led_thread.start()
    button_thread.start()
    try:
        while True:
            if state == 1:
                stop_blinking.set()
                interrupt_callback()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()