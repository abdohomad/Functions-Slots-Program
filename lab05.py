########################################################################
##
# CS 101 Lab
## Program #
# Name
# Email
##
# PROBLEM : Describe the problem
##
# ALGORITHM :
# 1. Write out the algorithm
##
# ERROR HANDLING:
# Any Special Error handling to be noted.  Wager not less than 0. etc
##
# OTHER COMMENTS:
# Any special comments
##
########################################################################

# import modules needed


from ast import Not
from email import message
from itertools import count
from math import fabs
import random


def keyboard_validator(message):
    """"Exceptions raised by keyboard_validator"""
    while True:
        try:
            value = input(f"{message}")
            value = int(value)
            return value
        except ValueError:
            print(" Please enter a valid number")


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    count = 0
    while True:
        count += 1
        end_game = input("Do you want to play again? ==>")
        end_game = end_game.upper()
        if (end_game == "YES" or end_game == "Y"):
            return True
        elif (end_game == "NO" or end_game == "N"):
            return False
        else:
            if count >= 2:
                return False
        print("You must enter Y/YES/N/NO to continue. Please try again")


def get_wager(bank: int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    message = "How many chips do you want to wager? ==>"
    wager_amount = keyboard_validator(message)
    while wager_amount < 1:
        print("The wager amount must be greater than 0. Please enter again.")
        wager_amount = keyboard_validator(message)
    while (wager_amount > bank):
        print(
            f"The wager amount cannot be greater than how much you have. {bank}")
        wager_amount = keyboard_validator(message)
    return wager_amount


def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    return num1, num2, num3


def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    match = 0
    if ((reela == reelb) and (reelb == reelc) and (reela == reelc)):
        match = 3
    elif ((reela == reelb) or (reela == reelc) or (reelb == reelc)):
        match = 2
    else:
        match = 0
    return match


def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    message = "How many chips do you want to start with? ==>"
    bank = keyboard_validator(message)
    while not (bank > 0 and bank < 101):
        if bank > 100:
            print("Too high a value, you can only choose 1 - 100 chips")
        if bank < 0:
            print("Too low a value, you can only choose 1 - 100 chips")
        bank = keyboard_validator(message)
    return bank


def get_payout(wager_amount, match):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    total = 0
    if (match == 3):
        total = wager_amount * 10
    elif match == 2:
        total = wager_amount * 3
    else:
        total = wager_amount * -1
    return total


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initial_amount = bank
        max_amount = initial_amount
        spin = 0

        # Replace with condition for if they still have money.
        while (bank > 0):

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > max_amount:
                max_amount = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin += 1

        print(f"You lost all {initial_amount} in  {spin} spins")
        print(f"The most chips you had was {max_amount}")
        playing = play_again()
