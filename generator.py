choice = input("Choose your way to convert (1 - roman to arabic; 2 - arabic to roman): ")
if choice == "1":
    nr=str(input("Choose a number between I and MMMCMXCIX: "))
    v = list(nr)
    l=len(v)
    nr_arabic = 0
    for i in range(0,l):
        if v[i] == "M" and ((v[i-1]!="C" and i-1>=0)or i==0):
            nr_arabic+=1000
        elif v[i] == "C" and i+1<l and v[i+1]=="M":
            nr_arabic+=900
            i+=1
        elif v[i] == "D" and ((v[i-1]!="C"and i-1>=0)or i==0):
            nr_arabic+=500
        elif v[i] == "C" and i+1<l and v[i+1]=="D":
            nr_arabic+=400
            i+=1
        elif v[i] == "C" and ((v[i - 1] != "X"and i-1>=0)or i==0):
            nr_arabic += 100
        elif v[i] == "X" and i+1<l and v[i+1]=="C":
            nr_arabic += 90
            i+=1
        elif v[i] == "L" and ((v[i - 1] != "X"and i-1>=0)or i==0):
            nr_arabic += 50
        elif v[i] == "X" and i+1<l and v[i+1]=="L":
            nr_arabic += 40
            i+=1
        elif v[i] == "X" and ((v[i - 1] != "I"and i-1>=0)or i==0):
            nr_arabic += 10
        elif v[i] == "I" and i+1<l and v[i+1]=="X":
            nr_arabic += 9
            i+=1
        elif v[i] == "V" and ((v[i - 1] != "I"and i-1>=0)or i==0):
            nr_arabic += 5
        elif v[i] == "I" and i+1<l and v[i+1]=="V":
            nr_arabic += 4
            i+=1
        elif v[i] == "I":
            nr_arabic += 1
    print(nr_arabic)
elif choice == "2":
    nr=int(input("Choose a number between 1 and 3999: "))
    if nr / 1000 >= 1:
        while nr / 1000 >= 1:
            print("M", end="")
            nr -= 1000
    if nr / 900 >= 1:
        print("CM", end="")
        nr -= 900
    if nr / 500 >= 1:
        print("D", end="")
        nr -= 500
    if nr / 400 >= 1:
        print("CD", end="")
        nr -= 400
    if nr / 100 >= 1:
        while nr / 100 >= 1:
            print("C", end="")
            nr -= 100
    if nr / 90 >= 1:
        print("XC", end="")
        nr -= 90
    if nr / 50 >= 1:
        print("L", end="")
        nr -= 50
    if nr / 40 >= 1:
        print("XL", end="")
        nr -= 40
    if nr / 10 >= 1:
        while nr / 10 >= 1:
            print("X", end="")
            nr -= 10
    if nr / 9 >= 1:
        print("IX", end="")
        nr -= 9
    if nr / 5 >= 1:
        print("V", end="")
        nr -= 5
    if nr / 4 >= 1:
        print("IV", end="")
        nr -= 4
    while nr > 0:
        print("I", end="")
        nr -= 1
    if nr == 0:
        print()
else:
    print("Your choice is not valid:(")