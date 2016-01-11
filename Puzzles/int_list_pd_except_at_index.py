'''
You have a list of integers and for each index you want to find the product of every integer except the integer at that index without using division.
'''

def findIntProductListExceptAtIndex(intList):
    '''
    Method to product int list except integer at index
    '''
    if intList is None or len(intList) < 2:
        return [1]

    # initialization
    listLength = len(intList)
    outputList = [1] * listLength

    leftPd = intList[0]
    rightPd = intList[listLength-1]

    for idx in range(1, listLength-1):
        # update left product
        outputList[idx] *= leftPd
        leftPd *= intList[idx]
        # update right product
        outputList[listLength-1-idx] *= rightPd
        rightPd *= intList[listLength-1-idx]

    outputList[0] = rightPd
    outputList[listLength-1] = leftPd
    return outputList

if __name__ == "__main__":
    print findIntProductListExceptAtIndex([1, 7, 3, 4])
    print findIntProductListExceptAtIndex([1, 7, 0, 4])

