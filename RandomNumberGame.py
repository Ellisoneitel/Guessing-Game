import random 
rand = int(random.randrange(1,10))
guess = int(input("Guess a number between 1 and 10: "))
Guesses = 1
while(rand != guess):
    if (rand > guess):
        guess = int(input("Guess a higher number: "))
    else:
        guess = int(input("Guess a lower number: "))
    Guesses += 1

if (Guesses < 3):
    print ("You're good at this! You guessed the number correctly in " + str(Guesses) + " guesses!")
elif(Guesses < 6):
    print ("You're averag. You guessed the number correctly in " + str(Guesses) + " guesses.")
else:
    print ("You're really terrible at this. It took you " + str(Guesses) + " guesses to find the correct number.")

