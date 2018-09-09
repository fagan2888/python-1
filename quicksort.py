import sys

print(sys.argv)
inputList = sys.argv[1].split(",")
print(inputList)

for j in range(0, len(inputList)):
    print("j=",j)           # j is the index
    print(inputList[j])   # print current element
    inputList[j] = int(inputList[j])

print(inputList)

def recursiveSorting(currentList):
    if(len(currentList) <= 1):
        return currentList
    else:
        lList = []
        rList = []
        pivotelement = currentList[-1]      # = currentList[len(currentList)-1], last element of the list
        print("Our Pivotelement is", pivotelement)
        for j in range(0, len(currentList)-1):
            currentElement = currentList[j]
            if(currentElement < pivotelement):
                lList.append(currentElement)
            else:
                rList.append(currentElement)
        print(lList, pivotelement, rList)
        lList = recursiveSorting(lList)
        rList = recursiveSorting(rList)
        partlySortedList = lList + [pivotelement] + rList
        print(partlySortedList)
        return partlySortedList

sortedList = recursiveSorting(inputList)

print(sortedList)
