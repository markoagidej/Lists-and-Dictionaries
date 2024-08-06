import time
import sys

# Task 1 Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.

def newSquareList(iterations):
    timeStart = time.time()
    squareList = [number**2 for number in range(1, iterations + 1)]
    timeEnd = time.time()
    print(f"Seconds to complete Task 1 list creation: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 1 function in bytes is {sys.getsizeof(squareList) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")
    return squareList

smallSqaureList = newSquareList(300)
medSqaureList = newSquareList(300000)
bigSqaureList = newSquareList(3000000)

'''
Anaylsis:
This is an O(n) operation. Technically as the input number grows, math takes longer for each calculation, but effectively we are still at O(n) time.
Space is also O(n). The space taken by the 2 time keeper variables is insignificant. 
'''

# Task 2 Implement a function to reverse a sublist within a list from index i to j (inclusive). Analyze the time and space complexity of this operation

def reverseSubList(parentList, subListStart, subListEnd):
    timeStart = time.time()
    subList = parentList[subListStart: subListEnd + 1]
    # revSubList = parentList[subListStart: subListEnd + 1][::-1]
    revSubList = subList[::-1]
    timeEnd = time.time()
    print(f"Seconds to complete Task 2 list creation: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 2 function in bytes is {sys.getsizeof(subList) + sys.getsizeof(revSubList) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")
    return revSubList

smallRevRange = reverseSubList(medSqaureList, 3, 7)
bigRevRange = reverseSubList(medSqaureList, 3, 299999)

'''
Anaylsis:
Time Complexity is O(n). Technically it is O(n+k) since a sublist is being made [O(k)], and then being reversed [O(n)]. This is reduced to O(n).
Space complexity is O(n). Effectively, two sublists are being stored [(O(2k))], but this reduces to O(n).
Note --- It was tested to create the reversed sublist with stacked list slicing as seen in the commented code above. This resulted in about 1/2 space taken, but roughly double runtime.
'''

# Task 3 Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

