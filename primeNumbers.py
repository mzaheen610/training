import logging 

#Configuring basics of the logger. Messages are logged to a file.

logging.basicConfig(filename='log_for_prime.log', filemode='a', format='%(name)s::%(levelname)s::%(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def isPrime(num):
    logger.warning("Checking if prime or not...")
    for i in range(2,num//2):
        if num%i == 0:
            logger.info("Oops..Number is not prime")
            return False
    logger.info("The number is found to be prime")  
    return True

def  getNumber():
    logger.info("Getting the number from a user")
    number = int(input("Enter a number to check if prime or not: "))
    return number

if __name__ == "__main__":
    num = getNumber()
    if isPrime(num):
        print("The number is prime")
    else:
        print("The number is not prime")
