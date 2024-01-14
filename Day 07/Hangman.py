import random
from art import stages, logo
from words import word_list


end_of_game = False
chosen_word = random.choice(word_list)
lives = len(stages)-1
print(logo)

display = []
for char in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in display:
        end_of_game = True
        print("You have won!")

    print(stages[lives])





