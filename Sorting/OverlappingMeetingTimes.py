'''
Find overlapping meeting times
'''


def condenseTimeSchedule(ipList):
    '''
    method to condense list of time schedules provided
    '''
    if ipList is None or len(ipList) < 2:
        return ipList


    # first sort the meetings by their starting time
    ipList.sort(key = lambda x: x[0])

    condensedList = [ipList[0]]

    for timeTuple in ipList[1:]:
        # if the starting time of current meeting is greater than ending time of previous meeting then there is no overlap
        # and they can not be merged; the current meeting is added as new interval to the condensed list
        if timeTuple[0] > condensedList[-1][1]:
            condensedList.append([timeTuple[0], timeTuple[1]])

        # else there is an overlap and we should update the previous meeting (in condensed list) by merging current meeting into it.
        # Since we know previous meeting's starting time is <= to current meeting's starting point (true because of sorting), we can
        # use it to serve as lower boound. In order to determine ending time of merged meeting, we will have to take the maximum ending
        # time of the two meetings.
        else:
            condensedList[-1] = (condensedList[-1][0], max(condensedList[-1][1], timeTuple[1])) # -1 refers to the last element in the list (in python)

    return condensedList


if __name__ == "__main__":

    print condenseTimeSchedule([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    print condenseTimeSchedule([(1, 2), (2, 3)])
    print condenseTimeSchedule([(1, 5), (2, 3)])
    print condenseTimeSchedule([(1, 10), (2, 6), (3, 5), (7, 9)])