import My_GPIO as mgp

mgp.StartRun()

while True:
    
    print ("Введите напряжение (от 0 до 255, -1 для выхода): ", end = "")
    inp = input().split()
    
    try:
        inp = int (inp[0])
    except:
        print ("Неверный ввод. Пожалуйста, соблюдайте правила ввода.")
        continue

    if (inp == -1):
        print ("Выход...")
        break
    elif (inp >= 0 and inp <= 255):
        mgp.num2dac (inp)
        # print ("OK: ", str (inp))
    else:
        print ("Неверный ввод. Пожалуйста, соблюдайте правила ввода.")

mgp.FinishRun()
