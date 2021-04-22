import RPi.GPIO as GPIO
import time

LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
DAC  = [26, 19, 13, 6, 5, 11, 9, 10]

port_in = 4
go_volts = 17

def StartRun():
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (LEDS, GPIO.OUT)
    GPIO.setup (DAC,  GPIO.OUT)
    GPIO.setup (go_volts,  GPIO.OUT)
    GPIO.setup (port_in, GPIO.IN)
    GPIO.output (go_volts, 1)

def FinishRun():
    GPIO.output (LEDS, 0)
    GPIO.output (go_volts, 0)
    GPIO.cleanup (LEDS)
    GPIO.cleanup (DAC)
    GPIO.cleanup (port_in)
    GPIO.cleanup (go_volts)

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

def PrintNumber (LEDS_modes, leds):

    # print (*LEDS_modes)
    for i_LED in range (len (LEDS)):
        GPIO.output (leds[i_LED], LEDS_modes[i_LED])
    # ToDo: Try GPIO.output (LEDS, LEDS_modes)

# -------------------------------------------------------------        

def lightNumber (number, leds):

    LEDS_modes = decToBinList (number)
    PrintNumber (LEDS_modes, leds)

# -------------------------------------------------------------

def num2dac (num, mode = 1):
    if (mode == 1):
        lightNumber (int (num), DAC)
    else:
        lightNumber (int (num), LEDS)

# -------------------------------------------------------------

def GetStatus():
    time.sleep (0.001)
    return GPIO.input (port_in) == GPIO.HIGH

# -------------------------------------------------------------

def VolumeBar (num):

    GPIO.output (LEDS, 0)
    num = (num + 16) // 32
    for i_LED in range (len (LEDS)):
        if (num == 0):
            return
        GPIO.output (LEDS[7 - i_LED], 1)
        num -= 1
