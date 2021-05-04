import random


def main():
    guess_limit = range(11)
    random_guess = random.choice(guess_limit)
    print("\n\nI guessed a number between 0-10 !\nFind out which one is!")
    tipp = int(input("\nWhat's your Guess? "))
    if tipp != random_guess:
        print("\nNOPE, missfired!!!")
    else:
        print("\nBULLSEYE! YOU are very ClEVER!!!!")
    print("I guessed to:", random_guess)
    replay()


def replay():
    print("\n\nDo you wanna try again?")
    rep_answ = str(input("Yes (y) / No (n): "))
    if rep_answ == str("y"):
        main()
    else:
        print("\n\tThanks for the Game! See-Ya!")


main()