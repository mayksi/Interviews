'''
In order to avoid re-visiting a web-page, a programmer implemented a simple version of dictionary 'visited'
where he would store as key each of the web page visited to web crawler.

What changes will you make in the program to make it more space efficient.
'''




class VisitedPage:
    '''
    a class to wrap around dictionary and provide convenience methods for checking visited page and inserting new ones
    '''

    def __init__(self):
        self.trie = [0, {}]

    def addUrl(self, url):
        '''
        Add url to dictionary
        '''
        if url is None or len(url) < 1:
            return

        currTuple = self.trie
        for ch in url:
            if not currTuple[1].has_key(ch):
                newTuple = [0, {}]
                currTuple[1][ch] = newTuple
            currTuple = currTuple[1][ch]
        currTuple[0] = 1

    def isUrlVisited(self, url):
        '''
        Add url to dictionary
        '''
        if url is None or len(url) < 1:
            return

        nodePresent = None
        currTuple = self.trie
        for ch in url:
            if not currTuple[1].has_key(ch):
                nodePresent = False
                break
            currTuple = currTuple[1][ch]

        if not nodePresent:
            nodePresent = currTuple[0]
        return True if nodePresent == 1 else False



    def printTrie(self):
        print self.trie

    def printNode(self, node):

        for (key, value) in node[1].items():
            print key, value[0]
            self.printNode(value)


if __name__ == "__main__":
    vs = VisitedPage()
    ipString = 'www.google.com'
    vs.addUrl(ipString)
    ipString = 'www.apple.com'
    vs.addUrl(ipString)

    vs.printTrie()

    print vs.isUrlVisited('www.apple.com')
    print vs.isUrlVisited('www.apple.co')
    print vs.isUrlVisited('www.google.com')

    vs.addUrl('www.apple.co')
    print vs.isUrlVisited('www.apple.co')
