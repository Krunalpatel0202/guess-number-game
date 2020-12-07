from random import randint
n = randint(10,30)
i=0
while i<5:
    m= int(input("guess the number:"))
    if m>n:
        print("greater")
    if m<n:
        print("smaller")
    elif m==n:
        print("congo, you won the game")
        break
if m>n or m<n:
    print("better luck next time")
else:
    print("you're good player")

