def get_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Please enter valid integers.")
        return get_numbers() 
