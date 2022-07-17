import time
def date():
    f = []
    print("Welcome to the yesterday")
    print("Please enter current date for example like this 12.05.1992 ")
    f = input()
    f = f.split(".")
    x = (int(f[0]))
    y = (int(f[1]))
    z = (int(f[2]))
    print('Current date is', x, '.', y, '.', z)
    if x != 1:
        x -= 1
    else:
        if x == 1 and y==1:
            x=31
            y=12
            z-=1
        if x == 1 and y==2:
            x=31
            y=1
        if x == 1 and y==3:
            if z % 400 == 0 or (z % 4 == 0 and z % 100 != 0):
                x=29
                y=2
            else:
                x=28
                y=2
        if x == 1 and y==4:
            x=31
            y=3
        if x == 1 and y==5:
            x=30
            y=4
        if x == 1 and y==6:
            x=31
            y=5
        if x == 1 and y==7:
            x=30
            y=6
        if x == 1 and y==8:
            x=31
            y=7
        if x == 1 and y==9:
            x=31
            y=8
        if x == 1 and y==10:
            x=30
            y=9
        if x == 1 and y==11:
            x=31
            y=10
        if x == 1 and y==12:
            x=30
            y=11

    print("The date yesterday was",x,".",y,".",z)

date()
time.sleep(20)
