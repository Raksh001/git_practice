import random

game_chooser = input("Please choose a game: 1 - Coin Flip, 2 - Dice: ")
while True:

    if game_chooser == "1":
        games_count = 0
        won_count = 0

        print("Welcome to the Coin Flip game!")

        while True:
            print("Dear user, please make your guess:")
            user_guess = input("Please, enter Heads or Tails: ")

            side = ""
            games_count += 1
            coin_flip = random.randrange(2)

            if coin_flip == 1:
                side = "Heads"
            else:
                side = "Tails"

            print("Coin flipped at: " + side)

            if user_guess == side:
                print("Your guess is right!")
                won_count += 1
            else:
                print("Sorry, better luck next time.")

            print("Your stats: won " + str(won_count) + " games over " + str(games_count) + " total games played.")

            print("Play again: ")
            key = input("Yes or No? ")
            print("\n")

            if key == "No":
                break
    elif game_chooser == "2":
        games_count = 0
        won_count = 0

        print("Welcome to the Dice game!")

        while True:
            print("Dear user, please make your guess (1-6):")
            user_guess = int(input("Please, enter your guess: "))

            games_count += 1
            dice_flip = random.randrange(1, 7)

            print("Dice flipped at: " + str(dice_flip))

            if user_guess == dice_flip:
                print("Your guess is right!")
                won_count += 1
            else:
                print("Sorry, better luck next time.")

            print("Your stats: won " + str(won_count) + " games over " + str(games_count) + " total games played.")

            print("Play again:")
            key = input("Yes or No? ")
            print("\n")

            if key == "No":
                break

    game_switch_input = input("Do you want to switch the game? ")
    if game_switch_input == "Yes":
        game_chooser = input("Please choose a game: 1 - Coin Flip, 2 - Dice: ")
    else:
        print("Thank you for playing!")
        print("\n")
        break