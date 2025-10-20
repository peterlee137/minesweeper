import random
mines=10
revealed=0
field=[["*" for i in range(8)] for j in range(8)]
minefield=[[0 for i in range(10)] for j in range(10)]

def start():
    show()
    setmine()
    print("there are 10 mines\n")
    game()

def show():
    for i in field:
        for j in i:
            print(j, end=" ")
        print("")

def setmine():
    planted=0
    for i in range(10):
        while planted==0:
            x=random.randint(1,8)
            y=random.randint(1,8)
            if minefield[y][x]==0:
                minefield[y][x]="X"
                planted=1
        planted=0
    for i in range(1,9):
        for j in range(1,9):
            if minefield[i][j]!="X":
                for ii in range(-1,2):
                    for jj in range(-1,2):
                        if minefield[i+ii][j+jj]=="X":
                            minefield[i][j]+=1

def flag(ypos,xpos):
    if field[ypos][xpos]=="*":
        field[ypos][xpos]="P"
    elif field[ypos][xpos]=="P":
        field[ypos][xpos]="*"
    else:
        print("cannot flag here")

def reveal(ypos,xpos):
    global revealed
    if 0<=ypos<=7 and 0<=xpos<=7:
        if minefield[ypos+1][xpos+1]=="X":
            field[ypos][xpos]="X"
            over()
        elif field[ypos][xpos]=="*":
            field[ypos][xpos]=minefield[ypos+1][xpos+1]
            revealed+=1
            if revealed==54:
                win()
            if field[ypos][xpos]==0:
                for i in range(-1,2):
                    for j in range(-1,2):
                        reveal(ypos+i,xpos+j)

def game():
    print("1) reveal\n2) flag/unflag\nwhat do you want to do:")
    a=int(input())
    print("\ninsert coordinates(x y):")
    x,y=map(int,input().split())
    if a==1:
        reveal(8-y,x-1)
    elif a==2:
        flag(8-y,x-1)
    else:
        print("invalid command\n")
        game()
    show()
    game()


def over():
    show()
    print("game over")
    quit()

def win():
    show()
    print("you win")
    quit()

start()