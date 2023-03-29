# # #hotel management system
# 3 clients- anuska, manas, yash
# total 6 files
# write a function that when executed takes as input client name

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c= int(input("enter 1 for exerxise and 2 for food\n"))
        if c==1:
            value= input("Type now\n")
            with open("Anu-exer.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully Written")
        elif c==2:
            value= input("Type now\n")
            with open("Anu-food.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully Written")

    elif k==2:
        c = int(input("enter 1 for exerxise and 2 for food\n"))
        if c == 1:
            value = input("Type now\n")
            with open("Manu-exer.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif c == 2:
            value = input("Type now\n")
            with open("Manu-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
    elif k==3:
        c = int(input("enter 1 for exerxise and 2 for food\n"))
        if c == 1:
            value = input("Type now\n")
            with open("Yash-exer.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif c == 2:
            value = input("Type now\n")
            with open("Yash-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
    else:
        print("Please enter valid input\n1-Anuska\n2-Manas\n3-Yash")

def getback(k):
    if k==1:
        c = int(input("enter 1 for exerxise and 2 for food\n"))
        if c==1:
            with open("Anu-exer.txt") as op:
                for i in op:
                    print(i, end="")
        elif c==2:
            with open("Anu-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c = int(input("enter 1 for exerxise and 2 for food\n"))
        if c == 1:
            with open("Manu-exer.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Manu-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c = int(input("enter 1 for exerxise and 2 for food\n"))
        if c == 1:
            with open("Yash-exer.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Yash-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Enter valid inputs only")

print("This is a Health management system: ")
a=int(input("Press 1 for lock the value and 2 for retrieve\n"))

if a==1:
    b=int(input("Enter 1 for Anuska, 2 for Manas and 3 for Yash\n"))
    take(b)
else:
    b=int(input("Enter 1 for Anuska's chart, 2 for Manas's chart and 3 for Yash's chart\n"))
    getback(b)
