from art import logo
import os

#clear desktop
def clear():
    os.system('cls' if os.name =='nt' else 'clear')

#loop trough list of bidders and find the highest bid
def find_highest_bid():
    highest_bid = 0
    highest_bidder = ""
    for bidder in list_of_bidders:
        if list_of_bidders[bidder] > highest_bid:
            highest_bid = list_of_bidders[bidder]
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")
other_bidders = True
list_of_bidders = {}

#games runs while we have bidders
while other_bidders:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))

    input_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    # add new bid
    list_of_bidders[name] = bid

    clear()

    #stop while
    if input_other_bidders == "no":
        other_bidders = False

find_highest_bid()












