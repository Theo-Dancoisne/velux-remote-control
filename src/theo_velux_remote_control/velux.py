import time
import RPi.GPIO as GPIO
from .config import *


GPIO.setmode(GPIO.BCM)

VELUX_PIN_OPEN = GPIO_PIN_OPEN
VELUX_PIN_STOP = GPIO_PIN_STOP 
VELUX_PIN_CLOSE = GPIO_PIN_CLOSE

GPIO.setup(VELUX_PIN_OPEN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(VELUX_PIN_STOP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(VELUX_PIN_CLOSE, GPIO.OUT, initial=GPIO.HIGH)


def v_cleanup():
    GPIO.cleanup()

def pulse(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    v_cleanup()

def v_open():
    pulse(VELUX_PIN_OPEN)

def v_close():
    pulse(VELUX_PIN_CLOSE)

def v_stop():
    pulse(VELUX_PIN_STOP)

