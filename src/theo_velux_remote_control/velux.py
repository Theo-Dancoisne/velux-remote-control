import time
import RPi.GPIO as GPIO
from dotenv import load_dotenv
import os


load_dotenv()

GPIO.setmode(GPIO.BCM)

VELUX_PIN_OPEN = int(os.getenv("GPIO_PIN_OPEN"))
VELUX_PIN_STOP = int(os.getenv("GPIO_PIN_STOP"))
VELUX_PIN_CLOSE = int(os.getenv("GPIO_PIN_CLOSE"))

GPIO.setup(VELUX_PIN_OPEN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(VELUX_PIN_STOP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(VELUX_PIN_CLOSE, GPIO.OUT, initial=GPIO.HIGH)


class Velux:
    
    def cleanup():
        GPIO.cleanup()
    
    def pulse(pin):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)
        Velux.cleanup()

    def open():
        Velux.pulse(VELUX_PIN_OPEN)

    def close():
        Velux.pulse(VELUX_PIN_CLOSE)

    def stop():
        Velux.pulse(VELUX_PIN_STOP)
