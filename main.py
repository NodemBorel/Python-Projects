import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} :"))
        if guess < random_number:
            print("Sorry to low")
        elif guess > random_number:
            print("Sorrry to high")
    print(f"You got it {guess} ,,, {random_number}")  
    
guess(10)       
