'''
In a given list of words which is alphabetically ordered by rotated by K units, find the rotation factor K.
(assuming no duplicate)
  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
'''

def findRotation(ipList):
    '''
    Find the rotation for the given list of words
    '''
    # @todo: basic error checking

    # initialization
    leftPtr = 0
    rightPtr = len(ipList)-1
    firstItem = ipList[0]
    while leftPtr < rightPtr:
        midPtr = (leftPtr+rightPtr)/2

        if firstItem < ipList[midPtr]:
            leftPtr = midPtr
        else:
            rightPtr = midPtr

        if leftPtr+1 == rightPtr:
            break

    return rightPtr


if __name__ == "__main__":

    words = ['karpatka', 'othellolagkage', 'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'zebra', 'zypher', 'asymptote', 'babka', 'baar', 'banoffee', 'engender', 'entail', 'entertain']
    print "Rotated distance: %s" % findRotation(words)

    words = ['bats', 'oats', 'amay']
    print "Rotated distance: %s" % findRotation(words)

    words = ['life', 'live', 'mars', 'mission', 'library']
    print "Rotated distance: %s" % findRotation(words)

    words = ['bb', 'able', 'aminity', 'azure', 'ba']
    print "Rotated distance: %s" % findRotation(words)

    words = ['bb', 'bc', 'bd', 'azure', 'ba']
    print "Rotated distance: %s" % findRotation(words)
