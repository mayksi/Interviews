'''
Given a list of integers, find 3 integers such their product is maximum of any triplet that can be formed from the list


'''


def findMaxTripletSum(ipList):
    '''
    Method to find maximum product that can be calcuated with 3 integers from the list
    '''
    if ipList is None or len(ipList) < 3:
        return False

    lowestNum = min(ipList[0], ipList[1])
    lowest2Pd = ipList[0]*ipList[1]
    highestNum = max(ipList[0], ipList[1])
    highest2Pd = ipList[0]*ipList[1]
    highest3Pd = -float('Inf')

    for num in ipList[2:]:
        highest3Pd = max(highest3Pd, lowest2Pd*num, highest2Pd*num)
        if num < lowestNum:
            lowest2Pd = lowestNum*num
            lowestNum = num
        elif num > highestNum:
            highest2Pd = highestNum*num
            highestNum = num

    return highest3Pd

if __name__ == "__main__":
    print findMaxTripletSum([-10, -10, 1, 3, 2])
    print findMaxTripletSum([1, 10, -5, 1, -100])
