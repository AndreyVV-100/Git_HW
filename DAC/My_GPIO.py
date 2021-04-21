import RPi.GPIO as GPIO
import time

# LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
LEDS = [26, 19, 13, 6, 5, 11, 9, 10]

def StartRun():
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (LEDS, GPIO.OUT)

def FinishRun():
    GPIO.output (LEDS, 0)
    GPIO.cleanup (LEDS)

# -------------------------------------------------------------

def lightUp (ledNumber, period, mode = 1):

    GPIO.output (LEDS[7 - ledNumber], mode)
    time.sleep (period)
    GPIO.output (LEDS[7 - ledNumber], mode ^ 1)

# -------------------------------------------------------------

def decToBinList (decNumber):
    lst = []
    # number = int (number)

    while (decNumber > 0):
        lst = [1 & decNumber] + lst
        decNumber = decNumber >> 1

    lst_need_len = 8 - len (lst)
    if (lst_need_len > 0):
        lst = [0] * lst_need_len + lst

    return lst

# -------------------------------------------------------------

def PrintNumber (LEDS_modes):

    # print (*LEDS_modes)
    for i_LED in range (len (LEDS)):
        GPIO.output (LEDS[i_LED], LEDS_modes[i_LED])
    # ToDo: Try GPIO.output (LEDS, LEDS_modes)

# -------------------------------------------------------------        

def lightNumber (number):

    LEDS_modes = decToBinList (number)
    PrintNumber (LEDS_modes)

# -------------------------------------------------------------

def num2dac(num):
    lightNumber (int (num))
