class calculator:
    def __init__(self) -> None:
        pass

    def add(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print("The sum is",num1 + num2)

    def subtract(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print("The difference is",num1 - num2)
    
    def multiply(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print("The product is",num1 * num2)
    
    def divide(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print("The division is",num1 / num2)


if __name__ == "__main__" :

    newCalculator = calculator()
    flag = True

    while flag == True:
        print("###CALCULATOR###")
        print("Choose an option::")
        print("\n ADD(1)")
        print("\n SUBTRACT(2)")
        print("\n MULTIPLY(3)")
        print("\n DIVIDE(4)")
        print("\n\n\n To exit, enter 'N'")

        option = str(input("::::"))

        if option == "1":
            newCalculator.add()
        elif option == "2":
            newCalculator.subtract()
        elif option == "3":
            newCalculator.multiply()
        elif option == "4":
            newCalculator.divide()
        elif option == "N":
            flag = False
        else:
            print("Enter a valid input!")







    
    


        