import My_GPIO as mgp

mgp.StartRun()

max_voltage = 3.3

while (True):

    l = 0
    r = 255

    while (r - l > 1):

        num = (l + r) // 2
        # print (num)
        mgp.num2dac (num)

        # if (input() == "1"):
        if (mgp.GetStatus()):
            l = num
            continue

        else:
            r = num

    # print ("Digital value: {num}, Analog value: {volt} V".format 
                        #    (num = r, volt = round (max_voltage * num / 255, 2)))
    mgp.VolumeBar (r)
    # mgp.time.sleep (0.01)

mgp.FinishRun()
