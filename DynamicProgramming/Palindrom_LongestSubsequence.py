'''
Write a function to calculate maximum length of a palindrome sub-sequence that can be formed from an array or a string.

Ex: Given 'AMNBASABSBADACA' should return 9 as ['A', 'A', 'A', 'B', 'S', 'B','A', 'A', 'A'] is the longest palindrome sub-sequence
'''

def printMatrix(matrix):
    for n in matrix:
        print n

def createMatrix(n, m):
    newMatrix = []
    for i in range(n):
        newRow = []
        for j in range(m):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix

def findLongestPalindromSS(ipList):
    '''
    Method to find longest common ss
    '''
    if ipList is None: # bad input
        return 0
    elif len(ipList) < 2: # list with 1 element
        return len(ipList)


    # initialization - create a matrix of nXn where n is the lenght of input list
    listLength = len(ipList)
    lookupTable = createMatrix(listLength, listLength)

    # for each sub-string of length == 1 in original string, mark lookup as 1
    # for each sub-string of length == 2 in original string, mark lookup as 2 if both characters are same
    # or as 1 if both characters are not same
    for idx in range(listLength):
        lookupTable[idx][idx] = 1
        if idx < listLength-1:
            lookupTable[idx][idx+1] = 2 if ipList[idx] == ipList[idx+1] else 1

    # for n > 2, following a bottom up approach we will build
    for lgts in range(3, listLength+1):
        for idx in range(lgts-1, listLength):
            i = idx-lgts+1
            if ipList[idx] == ipList[i]:
                lookupTable[i][idx] = lookupTable[i+1][idx-1] + 2
            else:
                lookupTable[i][idx] = max(lookupTable[i][idx-1], lookupTable[i+1][idx])

    print "Longest palindromic sub-sequence for '%s' is of length: %s" % (ipList, lookupTable[0][-1])
    return lookupTable[0][-1]

if __name__ == "__main__":

    assert 5 == findLongestPalindromSS('PAYBZBA'), "Longest sub-sequence palindrome of length 5: ['A', 'B', 'Z', 'B', 'A']"
    assert 9 == findLongestPalindromSS('AMNBASABSBADACA'), "Longest sub-sequence palindrome of length 9: ['A', 'A', 'A', 'B', 'S', 'B','A', 'A', 'A']"


