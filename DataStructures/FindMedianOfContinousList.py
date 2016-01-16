'''

'''


import heapq

class ContinousMedian():
    '''
    Class with methods for continour median
    '''

    def __init__(self):
        '''
        Class constructor
        '''
        self.streamMaxHeap = [] # stores lower half of the stream
        self.maxHeapLen = 0
        self.streamMinHeap = [] # stores upper half os the stream
        self.minHeapLen = 0

    def _pushToMaxHeap(self, num):
        num = -1*num
        heapq.heappush(self.streamMaxHeap, num)
        self.maxHeapLen += 1

    def _popFromMaxHeap(self):
        num = None
        if self.maxHeapLen > 0:
            num = -1*heapq.heappop(self.streamMaxHeap)
            self.maxHeapLen -= 1
        return num

    def _peekMaxHeap(self):
        num = None
        if self.maxHeapLen > 0:
            num = -1*self.streamMaxHeap[0]
        return num

    def _pushToMinHeap(self, num):
        heapq.heappush(self.streamMinHeap, num)
        self.minHeapLen += 1

    def _popFromMinHeap(self):
        num = None
        if self.minHeapLen > 0:
            num = heapq.heappop(self.streamMinHeap)
            self.minHeapLen -= 1
        return num

    def _peekMinHeap(self):
        num = None
        if self.minHeapLen > 0:
            num = self.streamMinHeap[0]
        return num

    def addIntToHeap(self, num):
        '''
        method to add number to appropriate heap
        '''
        # add the element to appropriate heap
        if self.maxHeapLen == 0 and self.minHeapLen == 0:
            self._pushToMaxHeap(num)
        elif self._peekMaxHeap() > num:
            self._pushToMaxHeap(num)
        else:
            self._pushToMinHeap(num)

        # re-balance
        if self.maxHeapLen - self.minHeapLen > 1:
            elem = self._popFromMaxHeap()
            self._pushToMinHeap(elem)
        elif self.minHeapLen -self.maxHeapLen > 1:
            elem = self._popFromMinHeap()
            self._pushToMaxHeap(elem)

    def findMedian(self):
        '''
        Method to find median for current stream of integers
        '''
        num = 1.0
        if self.maxHeapLen == 0 and self.maxHeapLen == self.minHeapLen:
            return 0
        elif self.maxHeapLen == self.minHeapLen:
            num =  (self._peekMaxHeap()+self._peekMinHeap())*1.0/2
        else:
            num *=  self._peekMaxHeap() if self.maxHeapLen > self.minHeapLen else self._peekMinHeap()
        return num

    def printHeaps(self):
        print "Max Heap -> %s und Min Heap -> %s" % (self.streamMaxHeap, self.streamMinHeap)


if __name__ == "__main__":
    fl = open('cm_ip.txt')
    totalNumInStream = int(fl.readline().strip())
    cm = ContinousMedian()
    for _ in range(totalNumInStream):
        num = int(fl.readline().strip())
        # print "num >>> %s" % num
        cm.addIntToHeap(num)
        # cm.printHeaps()
        print cm.findMedian()
        # print "<<<<<<<<>>>>>>>>>>"

'''
94455.0
57505.0
20555.0
36840.0
53125.0

'''

