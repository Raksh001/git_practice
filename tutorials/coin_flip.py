import random
on_off = True

correct_guesses = 0
incorrect_guesses = 0

while on_off:
   print("Which guessing game do you want to play? (Coin Flip or Dice Roll)")
game = str(input())

if game == "Coin Flip":
    guess = ""

    while guess != "Heads" and guess != "Tails":
        print("Type your guess, Heads or Tails")
        guess = str(input())

        if guess != "Heads" and guess != "Tails":
            print("Please type either 'Heads' or 'Tails'")

    if guess == "Heads":
        print("Your Guess: Heads")
    else:
        print("Your Guess: Tails")

    answer = ""

    random_number = random.randint(1, 2)

    if random_number == 1:
        answer = "Heads"
    elif random_number == 2:
        answer = "Tails"

    print("Answer: " + answer)

    if guess == answer:
        correct_guesses += 1
        print("Your guess was corret!")
    else:
        incorrect_guesses += 1
        print("Sorry, your guess was incorrect.")

    total_guesses = correct_guesses + incorrect_guesses

    print("Total Guesses: " + str(total_guesses))
    print("Total Correct Guesses: " + str(correct_guesses))

    continue_answer = ""

    while continue_answer != "yes" and continue_answer != "no":
        print("Do you want to continue? (yes or no)")
        continue_answer = str(input())

        if continue_answer != "yes" and continue_answer != "no":
            print("Please type either 'yes' or 'no'")

    if continue_answer == "no":
        on_off = False

elif game == "Dice Roll":
    guess = ""

    while guess != "1" and guess != "2" and guess != "3" and guess != "4" and guess != "5" and guess != "6":
        print("Type your guess, 1-6")
        guess = str(input())

        if guess != "1" and guess != "2" and guess != "3" and guess != "4" and guess != "5" and guess != "6":
            print("Please type either 1, 2, 3, 4, 5 or 6")

    print("Your Guess: " + guess)

    answer = str(random.randint(1, 6))

    print("Answer: " + answer)

    if guess == answer:
        correct_guesses += 1
        print("Your guess was corret!")
    else:
        incorrect_guesses += 1
        print("Sorry, your guess was incorrect.")

    total_guesses = correct_guesses + incorrect_guesses

    print("Total Guesses: " + str(total_guesses))
    print("Total Correct Guesses: " + str(correct_guesses))

    continue_answer = ""

    while continue_answer != "yes" and continue_answer != "no":
        print("Do you want to continue? (yes or no)")
        continue_answer = str(input())

        if continue_answer != "yes" and continue_answer != "no":
            print("Please type either 'yes' or 'no'")

    if continue_answer == "no":
        on_off = False

else:
    print("Please type either 'Coin Flip' or 'Dice Roll'")