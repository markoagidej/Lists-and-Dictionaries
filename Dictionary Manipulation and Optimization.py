import time
import sys

# Task 1 Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time and space complexity of this operation.

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

def mergeDicts(dict1, dict2):
    timeStart = time.time()
    dict1.update(dict2)
    timeEnd = time.time()
    print(f"Seconds to complete Task 1: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 1 function in bytes is: {sys.getsizeof(dict1) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

mergeDicts(dict1, dict2)

'''
Anaylsis:
Time Complexity is O(n).
Space Complexity is O(n). Space is only increaded by the size of the second dictionary.

'''

# Task 2 Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time and space complexity of this operation.

dict3 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

dict4 = {
    'c': 4,
    'd': 5,
    'e': 6,
}

def findDictIntersect(dict1, dict2):
    timeStart = time.time()
    intersetDict = {}
    for key, value in dict1.items():
        if key in dict2:
            intersetDict[key] = [value, dict2[key]]
    timeEnd = time.time()
    print(intersetDict)
    print(f"Seconds to complete Task 2: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 2 function in bytes is: {sys.getsizeof(intersetDict) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")


findDictIntersect(dict3, dict4)
'''
Anaylsis:
Time Complexity is O(n). The nested "if in" statement is O(1).
Space Complexity is O(n). The result is essentially a sublist of the 2 dictionaries. 

'''

# Task 3 Implement a function to count the frequency of each unique word in a list using a dictionary. Analyze the time and space complexity of this operation.

def wordCounter(wordList):
    timeStart = time.time()
    resultDict = {}
    for word in wordList:
        if word in resultDict:
            resultDict[word] += 1
        else:
            resultDict[word] = 1
    timeEnd = time.time()
    print(f"Seconds to complete Task 1: {timeEnd - timeStart: .7f}")
    print(f"Size of Task 1 function in bytes is: {sys.getsizeof(resultDict) + sys.getsizeof(timeStart) + sys.getsizeof(timeEnd)}")

'''
Anaylsis:
Time Complexity is O(n). One operation is performed for every entry in the data set.
Space Complexity is O(n). This reflects teh worst case scenario in which every word in the word list is different.
'''
