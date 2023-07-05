import random

def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("\nEnter a number: "))
        if guess < random_number:
            print("To low!!")
        elif guess > random_number:
            print("To high!!")
    print(f"You guessed the number {guess} \n")

guess_number(15)                