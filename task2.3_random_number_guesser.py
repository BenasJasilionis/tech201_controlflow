variable = 7
guess_count = 0

while guess_count != 3:
    guess = input("Guess the whole number between 1 and 20!")
    if guess.isdigit()  and int(guess) < 1 and int(guess) > 20:
        print("Please guess a whole number between 1 and 20")
    elif int(guess) == variable:
        print("You have guessed the correct number!")
        break
    elif int(guess) != variable:
        guess_count += 1
        print(f"You have used {guess_count} out of 3 guesses so far try again !")

print(" You have used up all your guesses, better luck next time!")









