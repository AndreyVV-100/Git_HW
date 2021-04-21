import My_GPIO as mgp

mgp.StartRun()
    
print ("Введите количество повторений: ", end = "")
inp = input().split()

try:
    inp = int (inp[0])
except:
    print ("Неверный ввод. Пожалуйста, соблюдайте правила ввода.")
    exit ()

if (inp < 0):
    print ("Неверный ввод. Пожалуйста, соблюдайте правила ввода.")
    exit ()

for i_iter in range (inp):
    
    for i_light in range (256):
        mgp.num2dac (i_light)
        mgp.time.sleep (0.005)
        # print (i_light)

    for i_light in range (255, -1, -1):
        mgp.num2dac (i_light)
        mgp.time.sleep (0.005)
        # print (i_light)

mgp.FinishRun()
