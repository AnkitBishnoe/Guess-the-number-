import random
n = random.randint(1,100)
print("Guess the number game")
a = -1
guesses = 0
while(a!=n and guesses < 5):
    a = int(input("guess the no:"))
    if(guesses < 4):
        if(a>n):
            print("lower no plz")
        elif(a<n):
            print("higher no plz")
    guesses = guesses + 1

if(a==n):
    print("you won!")
    print(f"you guessed the no {n} in {guesses} attempts.")
else:
    print("you lost!")
    print(f"The number was {n}.")