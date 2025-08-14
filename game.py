import random

def main():

    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            else:
                break
        except ValueError:
            continue

    while True:
        try:
            guess_val = int(input("Guess: "))
            guess = random.randint(1,n)


            if guess_val < guess:
                print("Too small!")
                continue
            elif guess_val > guess:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        except ValueError:
            continue

main()