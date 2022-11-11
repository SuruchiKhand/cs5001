def main():

    # given constant variable
    one_liter_less_cost = 0.10
    one_liter_more_cost = 0.25

    # receiving input from the user
    one_liter_less_num = int(input("How many containers that are one lite or less? "))
    one_liter_more_num = int(input("How many containers that are one liter or more? "))

    # performin the arithmetic calculations
    total_refund = float((one_liter_less_cost * one_liter_less_num) + (one_liter_more_cost * one_liter_more_num))

    # providing output to user
    print(f" Your total refund is {total_refund:.2f}")

if __name__ == "__main__":
    main()