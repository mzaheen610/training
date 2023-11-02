import logging 

#Configuring basics of the logger. Messages are logged to a file.

logging.basicConfig(filename='log_for_even_odd.log', filemode='w', format='%(name)s:%(levelname)s:%(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def find_even_numbers(numbers):
    even = [i for i in numbers if i%2 == 0 ]
    logger.debug("Finding the even numbers upto the given list")
    return even

def find_odd_numbers(numbers):
    odd = [i for i in numbers if i%2 != 0 ]
    logger.debug("Finding the odd numbers from the given list")
    return odd

def get_numbers():
    logger.info("User is entering the list here")
    userInput = input("Enter the list to find even and odd numbers: ")
    values = userInput.split()
    list1 = [int(num) for num in values]
    logger.debug("Number list is returned")
    return list1

if __name__ == "__main__":

    userList = get_numbers()
    logger.debug("Got the list of numbers from user")

    evenNumbers = find_even_numbers(userList)
    oddNumbers = find_odd_numbers(userList)

    logger.debug("Found even and odd numbers from the users list")

    print("The even numbers are ::", evenNumbers)
    print("The odd numbers are ::", oddNumbers)
    
    logger.warning("Mission Complete")

