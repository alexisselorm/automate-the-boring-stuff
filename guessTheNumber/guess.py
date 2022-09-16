import random

print("Hello, what is your name")
name = input()
secretNumber = random.randint(1,20)
print('Well '+name+' I am thinking of a number between 1 and 20 inclusive')

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break #The condition is for the correct guess

if guess == secretNumber:
    print("Good job. "+name+" you guessed my number in "+str(guessesTaken)+" guesses" )
else:
    print("Nope I was thinking of "+str(secretNumber))
