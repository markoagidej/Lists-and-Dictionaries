import time
import sys

# Task 1 Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.

def newSquareList(iterations):
    timeStart = time.time()
    squareList = [number**2 for number in range(1, iterations + 1)]
    timeEnd = time.time()
    print(f"Seconds to complete this list creation: {timeEnd - timeStart: .7f}")
    print(f"Size of this function in bytes is {sys.getsizeof(squareList) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

newSquareList(300)
newSquareList(300000)
newSquareList(3000000)

'''
Anaylsis:
This is an O(n) operation. Technically as the input number grows, math takes longer for each calculation, but effectively we are still at O(n) time.
Space is also O(n). The space taken by the 2 time keeper variables is insignificant. 
'''

# Task 2 Implement a function to reverse a sublist within a list from index i to j (inclusive). Analyze the time and space complexity of this operation



# Task 3 Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

