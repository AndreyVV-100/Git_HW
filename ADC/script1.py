# import My_GPIO as mgp

max_voltage = 3.3

# mgp.StartRun()

while (True):

    print ("Enter value (-1 to exit) > ", end = "")
    
    try:
        num = int (input())
        
    except:
        print ("Wrong input!")
        continue

    if (num == -1):
        print ("Exit...")
        break

    if (num < 0 or num > 255):
        print ("Wrong input!")
        continue

    # mgp.num2dac (num)
    print ("{num} = {volt}V".format (num = num, volt = round (max_voltage * num / 255, 2)))

# mgp.FinishRun()
