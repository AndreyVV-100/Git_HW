import RPi.GPIO as GPIO
import time

LEDS = [21, 20, 16, 12, 7, 8, 25, 24]

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

def blink (ledNumber, blinkCount, blinkPeriod):

    for i_blink in range (blinkCount):
        lightUp (ledNumber, blinkPeriod)
        if (i_blink < blinkCount - 1):
            time.sleep (blinkPeriod)

# -------------------------------------------------------------

# mode 1 == Light
# mode 0 == Dark

def RunningLEDs (mode, count, period):

    GPIO.output (LEDS, mode ^ 1)

    for i_iter in range (count):
        for i_LED in range (len (LEDS)):
            lightUp (i_LED, period, mode)

def runningLight (count, period): 
    RunningLEDs (1, count, period)
    
def runningDark (count, period):
    RunningLEDs (0, count, period)

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

# -------------------------------------------------------------        

def lightNumber (number):

    LEDS_modes = decToBinList (number)
    PrintNumber (LEDS_modes)

# -------------------------------------------------------------

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

# -------------------------------------------------------------

def ChangingBright (ledNumber, period = 2, fineness = 100):

    led = GPIO.PWM (LEDS[7 - ledNumber], 100)
    led.start (0)

    for i_time in range (fineness):
        # print (i_time /fineness)
        led.ChangeDutyCycle (100 * i_time / fineness)
        time.sleep (period / 2 / fineness)

    for i_time in range (fineness, 0, -1):
        # print (i_time /fineness)
        led.ChangeDutyCycle (100 * i_time / fineness)
        time.sleep (period / 2 / fineness)

    led.stop()
