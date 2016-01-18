'''
Reverse a linked list given the head of the list with following Node structure:

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None
'''
import sys

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.listSize = 0

    def addNode(self, value):
        newNode = ListNode(value)
        if self.head is not None:
            newNode.next = self.head
        self.listSize += 1
        self.head = newNode

    def reverseList(self):
        if self.listSize < 2:
            return

        prevNode = self.head
        currNode = prevNode.next
        nextNode = currNode.next

        prevNode.next = None
        while nextNode is not None:
            # reverse
            currNode.next = prevNode

            # increment
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next

        currNode.next = prevNode
        self.head = currNode


    def printList(self):
        currNode = self.head
        while currNode is not None:
            sys.stdout.write("-> %s " %currNode.value)
            currNode = currNode.next
        print ""


if __name__ == "__main__":


    # case 0: No Node
    ll = LinkedList()
    ll.printList()
    ll.reverseList()
    ll.printList()

    # case 1: 1 Node
    ll = LinkedList()
    ll.addNode(5)
    ll.printList()
    ll.reverseList()
    ll.printList()

    # case 2: >1 Nodes
    ll = LinkedList()
    ll.addNode(5)
    ll.addNode(1)
    ll.addNode(8)
    ll.addNode(9)

    ll.printList()
    ll.reverseList()
    ll.printList()