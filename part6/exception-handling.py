def sum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1 + num2)
    else:
        print("Data type was not a number for the parameters.")


number1 = input("Enter a number: ")

sum(number1, 12)
