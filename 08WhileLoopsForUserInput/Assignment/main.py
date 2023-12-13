import random

def number_guesser():
    secretnumber = random.randint(1, 10)
    iscorrect = False

    
    while iscorrect == False :
        print("Guess the secret number!")
        response = int(input())
        if response > secretnumber :
            print("Too high")
        elif response < secretnumber :
            print("Too low")
        elif response not in [1,2,3,4,5,6,7,8,9,0,10]:
            print("Not valid")
        elif response == secretnumber :
            print("Correct!")
            iscorrect = True


def number_guesser_with_lives() :
    secretnumber = random.randint(1, 10)
    iscorrect = False
    lives = 3
    
    while iscorrect == False :
        print("Guess the secret number!")
        response = int(input())
        if lives == 0 :
            print("You LOSE")
            iscorrect = True
        elif response > secretnumber :
            print("Too high")
            lives = lives -1
        elif response < secretnumber :
            print("Too low")
            lives = lives -1
        elif response not in [1,2,3,4,5,6,7,8,9,0]:
            print("Not valid")
        elif response == secretnumber :
            print("Correct!")
            iscorrect = True

def vending_machine() :
    amountdue = 50
    nickel = 5
    dime = 10
    quarter = 25

    while amountdue > 0 :
        print("Amount due:", amountdue)
        response = int(input())
        if response == nickel :
            amountdue = amountdue - nickel
        elif response == dime :
            amountdue = amountdue - dime
        elif response == quarter : 
            amountdue = amountdue - quarter
    if amountdue == 0 :
        print("Thank You!")
    elif amountdue < 0 :
        print("Change given:", (amountdue * -1))


def hangman() : 
    words : ["tower","fortnite","computer"]
    randomgen = random.randint(0,2)
    randomword = words[randomgen]
    blankcount = randomword.count()
    return blankcount
hangman()
