from random import randint
print("\n\n||----||MINESWEEPWER||----||")
SPOT1 = 1
SPOT2 = 2
SPOT3 = 3
SPOT4 = 4
print("\n\n",SPOT1,SPOT2,"\n",SPOT3,SPOT4)
mine = "M"
picker = randint(1, 4)
if picker == 1:
    SPOT1 = mine
elif picker == 2:
    SPOT2 = mine
elif picker == 3:
    SPOT3 = mine
elif picker == 4:
    SPOT4 = mine
else:
    print("ERROR 1- NUMBER CHOSEN ISN'T DEFINED")

gameStatus = True
while gameStatus == True:


    PLAYERinput = int(input("\nChoose a space:"))
    if PLAYERinput == 1:
        print("\n\n", "1", "2", "\n", "3", "4")
        print(SPOT1)
        if SPOT1 == mine:
            gameStatus = False
            print("\n\n", SPOT1, SPOT2, "\n", SPOT3, SPOT4)

        pass
    elif PLAYERinput == 2:
        print("\n\n", "1", "2", "\n", "3", "4")
        print(SPOT2)
        if SPOT2 == mine:
            gameStatus = False
            print("\n\n", SPOT1, SPOT2, "\n", SPOT3, SPOT4)

        pass
    elif PLAYERinput == 3:
        print("\n\n", "1", "2", "\n", "3", "4")
        print(SPOT3)
        if SPOT3 == mine:
            gameStatus = False
            print("\n\n", SPOT1, SPOT2, "\n", SPOT3, SPOT4)

        pass
    elif PLAYERinput == 4:
        print("\n\n", "1", "2", "\n", "3", "4")
        print(SPOT4)
        if SPOT4 == mine:
            gameStatus = False
            print("\n\n", SPOT1, SPOT2, "\n", SPOT3, SPOT4)



        pass
    else:
        print("ERROR 2- NUMBER DOESNT EXIST")
        print("\n\n", "1", "2", "\n", "3", "4")

        pass



print("\n\n|----------|GAME|----------|")
print("|----------|OVER|----------|")











