'''
Movie scheduling problem

Problem: Movie Scheduling Problem
Input: A set I of n intervals on the line.
I = [(1, 5), (3, 15), (7, 10), (5, 16), (13, 14), (11, 15), (16, 20)]

Output: What is the largest subset of mutually non-overlapping intervals which can be selected from I?
O = [(1, 5), (7, 10), (13, 14), (16, 20)]
'''


def findMaxNonOverlappingMoviesSchedule(movieTimingLists):
    '''
    Method to compute largest subset of non-overlapping intervals
    '''
    if movieTimingLists is None:
        return 0
    elif len(movieTimingLists) < 2:
        return len(movieTimingLists)

    # sort the movie time lists
    movieTimingLists.sort(key = lambda x: x[1])

    nonOverlappingTimeIntervals = [movieTimingLists[0]]
    for timing in movieTimingLists:
        if timing[0] >= nonOverlappingTimeIntervals[-1][1]:
            nonOverlappingTimeIntervals.append(timing)
    print "Longest non-overlapping intervals: %s" % nonOverlappingTimeIntervals
    return nonOverlappingTimeIntervals

if __name__ == "__main__":
    assert  [(1, 5), (7, 10), (13, 14), (16, 20)] == findMaxNonOverlappingMoviesSchedule([(1, 5), (3, 15), (7, 10), (5, 16), (13, 14), (11, 15), (16, 20)])

