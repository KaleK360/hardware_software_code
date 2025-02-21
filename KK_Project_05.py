
def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def main():
    print("Welcome to the Number Addition Program! This program will help you add two whole numbers. You can keep adding numbers until you choose to exit.")

    while True:
        num1 = get_valid_number("Enter the first number: ")

        num2 = get_valid_number("Enter the second number: ")

        result = num1 + num2
        print(f"\nThe sum of {num1} and {num2} is: {result}")

        while True:
            choice = input("\nWould you like to add more numbers? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'")

        if choice == 'no':
            print("\nThank you for using the Number Addition Program!")
            break

if __name__ == "__main__":
    main()
