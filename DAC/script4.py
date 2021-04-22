# import My_GPIO as mgp
from scipy.io import wavfile
import wave
import time

# samplerate, data = wavfile.read ("ssound.wav")
# print (samplerate)
wav = wave.open("sound.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
content = wav.readframes(nframes)

print (framerate)

# mgp.StartRun()

for i_music in content:
    # mgp.num2dac (i_music)
    print (i_music)
#     # mgp.num2dac ((32768 - i_music[1]) % 256)
#     # print ((32768 - i_music[0]) // 256, (32768 - i_music[1]) // 256)
    # time.sleep (1 / framerate)

# mgp.FinishRun()

# data1 = [i[0] for i in data]
# data2 = [i[1] for i in data]

# print ( min (data1), max (data1))
# print ( min (data2), max (data2)) 
