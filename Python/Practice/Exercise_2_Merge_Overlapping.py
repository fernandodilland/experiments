# Exercise obtained from the Internet, solved for practice.
# Programmed by: Fernando Dilland Mireles Cisneros

"""Arrays: Merge overlapping intervals
You are given an array (list) of interval pairs as input where each interval has
a start and end timestamp. The input array is sorted by starting timestamps. You
are required to merge overlapping intervals and return a new output array.

Consider the input array below. Intervals (1, 5), (3, 7), (4, 6), (6, 8) are
overlapping so they should be merged to one big interval (1, 8). Similarly,
intervals (10, 12) and (12, 15) are also overlapping and should be merged to
(10, 15).

Try it yourself before reviewing the solution and explanation.
"""

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def merge_intervals(v):
    result = v
    return result

originalArray = [(1, 5), (3, 7), (4, 6), (6, 8)]
print("Original array 1: ", originalArray)
originalArray2 = [(10, 12),(12, 15)]
print("Original array 2: ", originalArray2)


def getElements(orArray):
    print("--- Worker ---")
    print("Working with: ",orArray)
    sizeOriginalArray=len(orArray)
    print("Size of list: ",sizeOriginalArray)

    ListFirstTuple = [] # List first 2 elements
    ListFirstTuple.append(orArray[0])
    print("First tuple:", ListFirstTuple)
    FirstElement = ListFirstTuple[0][0]
    print("First element:", FirstElement)

    ListFinalTuple = [] # List finals 2 elements
    ListFinalTuple.append(orArray[sizeOriginalArray-1])
    print("Final tuple:", ListFinalTuple)
    ElementFinal = ListFinalTuple[0][1]
    print("Final element:", ElementFinal)
    
    return([FirstElement,ElementFinal])

print("\nWorking with Array 1...")
elementsArray=getElements(originalArray)

print("\nWorking with Array 2...")
elementsArray2=getElements(originalArray2)

print("\nResult 1:",merge_intervals(elementsArray))
print("Result 2:",merge_intervals(elementsArray2))