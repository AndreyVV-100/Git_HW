import My_GPIO as mgp
import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100
sleep = 1 / samplingFrequency
frequency = 0.5

time    = np.arange (0, 1 / frequency, sleep)
voltage = np.uint8 (127 * (np.sin (time * frequency * 2 * np.pi) + 1) + 1)

fig = plt.figure (figsize = (7, 7))
ax  = fig.add_subplot (1,1,1)

ax.plot (time, voltage, linewidth = 3, alpha = 0.5, label = "$U (t)$", color = "blue")
ax.scatter (time, voltage, s = 40, marker = "_", color = "red")

ax.set_title ("График $U (t)$", fontsize = 20)
ax.set_ylabel ('$U$, ед', fontsize = 20)
ax.set_xlabel ('$t$, с',  fontsize = 20)

ax.grid (True)
ax.legend()
plt.savefig ("time-sin.pdf")

mgp.StartRun()

for i_repeat in range (10):
    for i_time in range (len (time)):
        mgp.num2dac (voltage[i_time])
        mgp.time.sleep (sleep)
        # print (voltage[i_time])

mgp.FinishRun()
