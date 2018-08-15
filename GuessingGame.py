import random

#generate digits and randommize
digits = list(range(10))
random.shuffle(digits)

#select just the first 3 of the new randomized list
myRandom = digits[:3]

#uncomment the random number just to check that the logic is correct
#print(myRandom)

print("Welcome to the guessing game! Try to guess what the 3 digit number is")

#set condition for looop
found = False

#logic for the game
while(not found):
    guess = int(input("What's your guess? "))

    #seperate into invdidual digits for easier evaluation
    d1 = int(guess/100)
    d2 = (int(guess/10)) %10
    d3 = guess % 10

    #both conditions are set to false at the beginning
    match1 = False
    match2 = False
    match3 = False
    close = False

    #check if there's a match or a close
    for i,x in enumerate(myRandom):
        if d1 == myRandom[i] and i == 0:
            match1 = True
        if d2 == myRandom[i] and i == 1:
            match2 = True
        if d3 == myRandom[i] and i == 2:
            match3 = True
        if d1 == myRandom[i] or d2 == myRandom[i] or d3 == myRandom[i]:
            close = True

    """
    priority list:
        1. Guessing the number correctly
        2. There is at least a match (number guessed correctly and correct position)
        3. There is at least a correct digit but wrong place
        4. None is correct
    """

    if match1 and match2 and match3:
        print("Correct! You guessed correctly!")
        found = True
    elif match1 or match2 or match3:
        print("There is at least a match")
    elif close:
        print("There is at least one correct digit but in the wrong place")
    else:
        print("You havent' guess any correctly.")

#closure for the game
print("Thanks for playing!")
