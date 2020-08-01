# lotto.py
import random
import time


select = str(input("Auto/Manual"))
lotto_auto = []
lotto_auto_number = random.randint(1, 100)
if select == "Auto":
    #time.sleep(3)
    for auto in range(7):
        #time.sleep(4)
        while lotto_auto_number in lotto_auto:
            lotto_auto_number = random.randint(1, 100)
        lotto_auto.append(lotto_auto_number)

elif select == "Manual":
    time.sleep(3)
    lotto_manual_number = list(map(int, input("Geben Sie 7 Zahlen: ").split()))

else:
    select = str(input("Auto/Manual"))

lotto_win = []
lotto_win_number = random.randint(1, 100)
for win in range(7):
    while lotto_win_number in lotto_win:
        lotto_win_number = random.randint(1, 100)
    lotto_win.append(lotto_win_number)

if select == "Auto":
    if lotto_win == lotto_auto:
        print("lucky")
    else:
        print("next...")
elif select == "Manual":
    if lotto_win == lotto_manual:
        print("lucky")
    else:
        print("next...")

re = str(input("If you want to repurchase yes or no:"))
if re == "yes":
    select = str(input("Auto/Manual"))
elif re == "no":
    print("bye")
else:
    re = str(input("If you want to repurchase yes or no:"))
