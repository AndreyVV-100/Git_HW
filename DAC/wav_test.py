import My_GPIO as mgp
from scipy.io import wavfile
import wave
import time
import numpy as np

mgp.StartRun()

wav = wave.open("ssound.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
content = wav.readframes(nframes)

samplingFrequency = 44100
sleep = 1 / samplingFrequency
frequency = 1

time    = np.arange (0, 1 / frequency, sleep)
voltage = np.uint8 (127 * (np.sin (time * frequency * 2 * np.pi) + 1) + 1)

def Test1():
    for i_music in voltage:
        mgp.num2dac (i_music)
        time.sleep (1 / framerate)

def Test2():
    for i_music in voltage:
        mgp.num2dac (i_music)
        time.sleep (0.5 / framerate)
        mgp.num2dac (0)
        time.sleep (0.5 / framerate)

mgp.FinishRun()
