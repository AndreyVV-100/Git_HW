# import RPi.GPIO as GPIO
import time

# mode 1 == Light
# mode 0 == Dark

LEDS = []

def lightUp (ledNumber, period, mode = 1):

    GPIO.output (ledNumber, mode)
    time.sleep (period)
    GPIO.output (ledNumber, mode ^ 1)

def blink (ledNumber, blinkCount, blinkPeriod):

    for i_blink in range (blinkCount):
        lightUp (ledNumber, blinkPeriod)
        if (i_blink < blinkCount - 1):
            time.sleep (blinkPeriod)

def RunningLEDs (mode, count, period):

    for i_LED in LEDS:
        GPIO.output (i_LED, mode ^ 1)

    for i_iter in range (count):
        for i_LED in LEDS:
            lightUp (i_LED, period, mode)

def runningLight (count, period): 
    RunningLEDs (1, count, period)
    
def runningDark (count, period):
    RunningLEDs (0, count, period)

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

def PrintNumber (LEDS_modes):

    print (*LEDS_modes)
    # for i_LED in range (len (LEDS)):
        # GPIO.output (LEDS[i_LED], LEDS_modes[i_LED])
        

def lightNumber (number):

    LEDS_modes = decToBinList (number)
    PrintNumber (LEDS_modes)

def runningPattern (pattern, direction, count = 8, period = 1):

# direction = 1 --- left
# direction = 0 --- right

    LEDS_modes = decToBinList (pattern)

    for i_iter in range (count):
        PrintNumber (LEDS_modes)
        time.sleep (period)
        if (direction):
            LEDS_modes =  LEDS_modes[1:]  + [LEDS_modes[0]]
        else:
            LEDS_modes = [LEDS_modes[-1]] +  LEDS_modes[:-1]

def ChangingBright (led, period = 1, fineness = 100):

    led.start (0)

    for i_time in range (fineness):
        print (i_time /fineness)
        led.ChangeDutyCycle (i_time / fineness)
        time.sleep (period / 2 / fineness)

    for i_time in range (fineness, 0, -1):
        # print (i_time /fineness)
        led.ChangeDutyCycle (i_time / fineness)
        time.sleep (period / 2 / fineness)

    led.stop()
