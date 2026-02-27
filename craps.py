from random import randint

player_win_numbers = (7, 11)
casino_win_numbers = (2, 3, 12)
goal_numbers = (4, 5, 6, 8, 9, 10)

def get_sum_of_dices():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1 + die2

def win_or_lose_cases(total):
    if total in player_win_numbers:
        return True
    elif total in casino_win_numbers:
        return False

def play_game():
    signal = input("Press Enter to roll the dice...")
    if signal == "":
        return get_sum_of_dices()
    else:
        print("Invalid input. Please press Enter to roll the dice.")
        return play_game()

# First roll (come-out roll)
sum_of_dices = play_game()
print(f"You rolled {sum_of_dices}")

if sum_of_dices in player_win_numbers + casino_win_numbers:
    if win_or_lose_cases(sum_of_dices):
        print("You win!")
    else:
        print("Sorry, you lose. Better luck next time! (The casino wins)")

elif sum_of_dices in goal_numbers:
    point = sum_of_dices
    print(f"Your point is {point}.")
    print(f"Keep rolling until you hit {point} again to win, or 7 to lose.")

    while True:
        sum_of_dices = play_game()
        print(f"You rolled {sum_of_dices}")

        if sum_of_dices == 7:
            print("Sorry, you lose. You rolled a 7 before hitting your point.")
            break
        elif sum_of_dices == point:
            print("You win!")
            break