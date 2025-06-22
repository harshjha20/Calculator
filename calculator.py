def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user for operation
    choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

    # Validate choice
    if choice in ['1', '2', '3', '4']:
        # Take two numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if choice == '1':
            print(f"The result of addition is: {num1 + num2}")
        elif choice == '2':
            print(f"The result of subtraction is: {num1 - num2}")
        elif choice == '3':
            print(f"The result of multiplication is: {num1 * num2}")
        elif choice == '4':
            # Check for division by zero
            if num2 != 0:
                print(f"The result of division is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")

# Run the calculator
calculator()
