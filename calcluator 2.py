import math

while True:
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    if choice == "6":
        num = float(input("Enter a number: "))
        print("Result:", math.sqrt(num))

    elif choice == "7":
        num = float(input("Enter the number: "))
        per = float(input("Enter the percentage: "))
        print("Result:", (num * per) / 100)

    elif choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == "5":
            print("Result:", num1 ** num2)

    else:
        print("Invalid choice. Please try again.")