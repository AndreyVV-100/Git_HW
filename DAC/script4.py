import My_GPIO as mgp
from scipy.io import wavfile
import numpy as np

samplerate, data = wavfile.read ("ssound.wav")

sleep = 1 / 44100
sound = np.array (data)
sound = np.int32 (sound[:,0])

mgp.StartRun()

print ("Wait...")

for i_music in range (len (sound)):
    sound[i_music] = (sound[i_music] + 32768) // 256

print ("Playing!")

for i_music in sound:
    mgp.num2dac (i_music)
    mgp.time.sleep (0)
    mgp.time.sleep (0)
    mgp.time.sleep (0)

mgp.FinishRun()

# data1 = [i[0] for i in data]
# data2 = [i[1] for i in data]

# print ( min (data1), max (data1))
# print ( min (data2), max (data2)) 
