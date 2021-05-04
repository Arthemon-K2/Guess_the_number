import random


def main():
    guess_limit = range(11)
    random_guess = random.choice(guess_limit)
    print("\n\nGondoltam egy számra 0-10 között!\nTaláld ki melyik lehet az!")
    tipp = int(input("\nTE melyik számra tippelsz? "))
    if tipp != random_guess:
        print("\nEz nem jött össze, NEM talált!!!")
    else:
        print("\nTeli találat! NAGYAON ÜGYES vagy!!!!")
    print("Erre gondoltam!", random_guess)
    replay()


def replay():
    print("\n\nMegpróbálod újra?")
    rep_answ = str(input("Igen (i) / Nem (n): "))
    if rep_answ == str("i"):
        main()
    else:
        print("\n\tKöszi, hogy játszottunk! Találkozunk legközelebb is! Bye!")


main()