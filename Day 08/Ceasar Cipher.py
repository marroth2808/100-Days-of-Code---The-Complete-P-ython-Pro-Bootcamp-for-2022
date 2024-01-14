
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(user_direction, old_text, shift_amount):
    new_text = ""
    for char in old_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            if user_direction == "encode":
                new_index = old_index + shift_amount
            elif user_direction == "decode":
                new_index = old_index - shift_amount
            new_text += alphabet[new_index]
        else:
            new_text += char
    print(new_text)

print(logo)

game_runs = True

while game_runs:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceasar(direction, text, shift)

    restart = input("Do you want to restart the caesars cipher? \n Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if restart == "no":
        game_runs = False






