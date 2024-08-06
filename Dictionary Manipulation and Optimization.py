import time
import sys

# Task 1 Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time and space complexity of this operation.

def mergeDicts(dict1, dict2):
    timeStart = time.time()
    dict1.update(dict2)
    timeEnd = time.time()
    print(f"Seconds to complete Task 1: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 1 function in bytes is: {sys.getsizeof(dict1) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

dict2 = {
    'c': 4,
    'd': 5,
    'e': 6,
}

mergeDicts(dict1, dict2)

'''
Anaylsis:
Time Complexity is O(n).
Space Complexity is O(n). Space is only increaded by the size of the second dictionary.

'''

# Task 2 Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time and space complexity of this operation.

# def findDictIntersect(dict1, dict2):
#     timeStart = time.time()
    
#     timeEnd = time.time()
#     print(f"Seconds to complete Task 1: {timeEnd - timeStart: .7f}")
#     print(f"Size of Task 1 function in bytes is: {sys.getsizeof() + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

'''
Anaylsis:

'''

# Task 3 Implement a function to count the frequency of each unique word in a list using a dictionary. Analyze the time and space complexity of this operation.

# def wordCounter():
#     timeStart = time.time()
    
#     timeEnd = time.time()
#     print(f"Seconds to complete Task 1: {timeEnd - timeStart: .7f}")
#     print(f"Size of Task 1 function in bytes is: {sys.getsizeof() + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

'''
Anaylsis:

'''
