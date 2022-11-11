def main():
    withdraw_amount = int(input("Please enter the amount you would like to withdraw: "))
    print("You are withdrawing $", withdraw_amount)
    print("This breaks down to: ", end= " ",)

    fifties = int(withdraw_amount // 50)
    fifties_remainder = withdraw_amount % 50
    print("", fifties, "fifties,", end= " ")

    twenties = int(fifties_remainder // 20)
    twenties_remainder = fifties_remainder % 20
    print("", twenties, "twenties,", end= " ")

    tens = int(twenties_remainder // 10)
    tens_remainder = twenties_remainder % 10
    print("", tens, "tens,", end= " ")

    fives = int(tens_remainder // 5)
    fives_remainder = tens_remainder % 5
    print("", fives, "fives,", end= " ")

    ones = int(fives_remainder // 1)
    ones_remainder = fives_remainder % 1
    print("", ones, "ones.")

if __name__ == "__main__":
    main()

# '''
# Test case #1:
# Input: $2
# Output: 0 fifties, 0 twenties, 0 tens, 0 fives, 2 ones

# Test case #2:
# Input: $27
# Output: 0 fifties, 1 twenties, 0 tens, 1 fives, 2 ones

# Test case #3:
# Input: $160
# Output: 3 fifties, 0 twenties, 1 tens, 0 fives, 0 ones
# '''
