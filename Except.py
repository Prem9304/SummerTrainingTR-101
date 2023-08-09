while True:
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        result = num1 + num2
        print("Sum:", result)
        break  # Exit the loop if input and addition are successful
    except ValueError:
        print("Invalid input. Please enter valid integers.")
