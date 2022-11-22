
# Let’s write a program that simulates a coin-flip game where we:
# Flip a “coin” a number of times
# Keep track of the number of “heads” and “tails”
# Print a report of the heads/tails for the user to see

import random

def flip_coin():
    number = random.randint(0, 201)
    if number % 2 == 0:
        return "HEADS"
    return "Tails"
    

def main():
    heads = 0
    tails = 0

    times = int(input("How many flips? "))
    if times > 50 or times < 5:
        times = 40

    index = 0
    while index < times:
        if flip_coin() == "HEADS":
            heads += 1

            print("Heads")
        else:
            tails += 1
            print("TAILS")

        result = flip_coin()
        if result == "Heads":
            heads += 1
        else:
            tails += 1
        print(result)
        index = index + 1
    
    print(f"For {times} flips, we got {heads} HEADS" f" and {tails} TAILS")

if __name__ == "__main__":
    flip_coin()
    main()