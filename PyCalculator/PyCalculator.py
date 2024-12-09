def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")

    while True:
        # Input from the user
        choice = input("\nEnter your choice (1/2/3/4/5 or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice == '5':
                    print(f"The result is: {num1 ** num2}")
            except ValueError:
                print("Error: Invalid input. Please enter numerical values.")
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    calculator()
