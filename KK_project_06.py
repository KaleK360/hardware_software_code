
def is_valid_binary(binary_str):
    return all(bit in '01' for bit in binary_str)

def binary_to_decimal(binary_str):
    if not is_valid_binary(binary_str):
        return None
    return int(binary_str, 2)

def decimal_to_binary(decimal_str):
    try:
        decimal = int(decimal_str)
        if decimal < 0:
            return None
        return bin(decimal)[2:]  # Remove '0b' prefix
    except ValueError:
        return None

def main():
    print("=== Number Conversion Program === This program converts numbers between decimal and binary formats. It will continue running until you choose to exit.")

    while True:
        print("\nSelect conversion type:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Thank you for using the conversion program!")
            break

        elif choice == '1':
            decimal_input = input("Enter a decimal number: ")
            result = decimal_to_binary(decimal_input)
            if result is not None:
                print(f"Binary equivalent: {result}")
            else:
                print("Error: Please enter a valid positive decimal number.")

        elif choice == '2':
            binary_input = input("Enter a binary number: ")
            result = binary_to_decimal(binary_input)
            if result is not None:
                print(f"Decimal equivalent: {result}")
            else:
                print("Error: Please enter a valid binary number (0s and 1s only).")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
