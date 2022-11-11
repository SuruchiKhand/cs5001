def main():
    field_length = float(input("Enter the length of the field: "))
    field_width = float(input("Enter the width of the field: "))

    field_area = field_length * field_width

    area_in_acres = field_area / 43560

    print(f" The area of the field is {area_in_acres:.3f} acres.")

if __name__ == "__main__":
    main()