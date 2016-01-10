'''
Find interval intersection from two list of intervals (that are sorted within the list)

# Intersection:
# a: [(5, 20), (30, 40), (50, 70)]
# b: [(10, 25), (35, 60), (90 , 100)]
# out: [(10, 20), (35, 40), (50, 60)]
'''

def findIntervalIntersection(listA, listB):
    '''
    Method to find overlapping sequence
    '''

    idxA, idxB, lenA, lenB = 0, 0, len(listA), len(listB)
    overlapInterval = []

    cnt = 0
    while idxA < lenA and idxB < lenB:
        currAElem = listA[idxA]
        currBElem = listB[idxB]

        if currBElem[0] >= currAElem[1]:
            idxA += 1
        elif currAElem[0] >= currBElem[1]:
            idxB += 1
        else:
            overlapInterval.append((max(currBElem[0], currAElem[0]), min(currAElem[1], currBElem[1])))
            if currBElem[1] <= currAElem[1]:
                idxB += 1

            if currAElem[1] <= currBElem[1]:
                idxA += 1

    return overlapInterval

if __name__ == "__main__":
    listA = [(5, 20), (30, 40), (50, 70)]
    listB = [(10, 25), (35, 60), (90 , 100)]
    assert  [(10, 20), (35, 40), (50, 60)] == findIntervalIntersection(listA, listB)