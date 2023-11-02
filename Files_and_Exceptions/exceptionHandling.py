### Handling Division by zero error 

def divide_numbers():
     num1 = input("Enter first number:")
     num2 = input("Enter second number:")

     try:
        result = int(num1) / int(num2)
        print(result)
     except ZeroDivisionError:
         print("You cannot divide by zero!")
    
### Handling File not found error

divide_numbers()

def read_file(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        msg = "Sorry. The file" + filename + " does not exist"
        print(msg)    
    else:
        for line in lines:
            print(line.strip())

read_file('Files_and_Exceptions\copiedText.txt')


    
