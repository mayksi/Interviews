'''
Given a (unsorted) list of building height of length 'N' and an integer 'K' number of buildings to choose from the list (in any order)
Find the minimum number of floors required to be build in the set of 'K' buildings so that the height of all the buildings in the set
are equal. (Note: You can only add floors to a building to make the height equal and floors can not be removed to do the same)

Example:
K = 3
Building Heights: [1, 5, 4, 2, 1]

Answer: 2
If you choose buildings at index 0, 3 and 4 then we get buildings [1, 2, 1]
In order to make heights equal for all the buildings in this set, we have to add 1 to 2 buildings of height 1
'''

def  minFloors(paintNum,  buidlingHeightList):
    '''
    function to calculate minimum number of floors to build
    '''
    # if 1 building is required to be painted then any building can be chosen
    # and we do not need to build any additional floors
    if paintNum <= 1:
        return 0

    # Sort the building by height
    # Sorting helps in efficiently calculating (in later step) floors required to build in current window
    # with the knowledge of floors required to build in previous window
    # by performing 1 addition, 1 multiplication and 2 subtractions
    buidlingHeightList.sort()
    totalBuildings = len(buidlingHeightList)

    # initialize 1st window's end index
    rightPtr = paintNum - 1 # since list is 0-index, subtract 1

    # calculate the number of floors required to build for the first window
    # window: sub-list of buildings of size 'paintNum'
    prevFloorsToBuild = 0
    for idx in range(rightPtr, -1, -1):
        # since buildings are sorted we can calculate # of floors required to build
        # for current building by subtracting it's height from max height
        # which is at the right most index of current window
        prevFloorsToBuild += buidlingHeightList[rightPtr] - buidlingHeightList[idx]

    # now move the window 1 step towards right and successively calculate min floors required to build
    minFloorsToBuild = prevFloorsToBuild
    for idx in range(rightPtr+1, totalBuildings):
        diffToLastMax = buidlingHeightList[idx] - buidlingHeightList[idx-1]

        # number of floors required to build in new window =
        # (floors required to build in previous window) +
        # (additional difference 'diffToLastMax' for (paintNum-1) floors) -
        # (floors required to be build for 1st building of last window)
        currFloorsToBuild = prevFloorsToBuild + \
                            (diffToLastMax*(paintNum-1)) - \
                            (buidlingHeightList[idx-1]-buidlingHeightList[idx-paintNum])

        minFloorsToBuild = min(minFloorsToBuild, currFloorsToBuild)
        prevFloorsToBuild = currFloorsToBuild

        # best case: when no floors are required to be built
        # we can break the for loop as we don't have to keep looking
        if minFloorsToBuild == 0:
            break

    return minFloorsToBuild

if __name__ == "__main__":
    fl = open("sp_ip.txt")

    testCases = int(fl.readline().strip())
    for _ in range(testCases):
        K = int(fl.readline().strip())
        buidlingHeightList = map(int, fl.readline().strip().split(' '))
        print K, buidlingHeightList
        print minFloors(K, buidlingHeightList)
