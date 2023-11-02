from concurrent.futures import ThreadPoolExecutor
import threading

def find_even_numbers(numbers):
    even = [i for i in numbers if i%2 == 0 ]
    print(even)
    print("Task Executed {}".format(threading.current_thread()))

    

def find_odd_numbers(numbers):
    odd = [i for i in numbers if i%2 != 0 ]
    print(odd)
    print("Task Executed {}".format(threading.current_thread()))

    

def main():
    executor = ThreadPoolExecutor(max_workers= 3)

    task1 = executor.submit(find_even_numbers,[1,2,3,4,5,6,7,8,9,10,11])
    task1 = executor.submit(find_even_numbers,[1,2,3,4,5,6,7,8,9,10,11])
    task2 = executor.submit(find_odd_numbers,[1,2,3,4,5,6,7,8,9,10,11])

if __name__ == "__main__":
    main()
