from Art import logo
import random

EASY = 10
HARD = 5
def set_difficulty():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif == "easy":
        return EASY
    elif dif == "hard":
        return HARD

def check_guess(user_number, answer, attemps):
    if user_number < answer:
        print("Too low")
        attemps -= 1
    elif user_number > answer:
        print("Too high")
        attemps -= 1
    else:
        print(f"You got it! The answer was {answer}")
    return attemps

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, answer, attempts)
        if guess != answer:
            print("Guess again")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return

game()








