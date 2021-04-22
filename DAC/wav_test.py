import My_GPIO as mgp
from scipy.io import wavfile
import wave
import time
import numpy as np

mgp.StartRun()

samplingFrequency = 256
sleep = 1 / samplingFrequency
frequency = 1

time    = np.arange (0, 1 / frequency, sleep)
voltage = np.uint8 (127 * (np.sin (time * frequency * 2 * np.pi) + 1) + 1)

def Test1():
    for i_music in voltage:
        mgp.num2dac (i_music)
        mgp.time.sleep (sleep)

def Test2():
    for i_music in voltage:
        mgp.num2dac (i_music)
        mgp.time.sleep (sleep)
        mgp.num2dac (0)
        mgp.time.sleep (sleep)

while True:
    Test2()
mgp.FinishRun()
