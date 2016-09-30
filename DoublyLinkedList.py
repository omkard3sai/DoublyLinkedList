from Node import Node


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def displayforward(self):
        displaytemp = self.head
        while displaytemp:
            print("->", end="")
            print(displaytemp.data, end="")
            displaytemp = displaytemp.next
        print("")

    def displaybackward(self):
        displaytemp = self.tail
        while displaytemp:
            print("<-", end="")
            print(displaytemp.data, end="")
            displaytemp = displaytemp.previous
        print("")

    def insertend(self, data):
        insert = Node(data)
        if self.isempty():
            self.head = insert
        else:
            self.tail.next = insert

        insert.previous = self.tail
        self.tail = insert
        return True

    def insertstart(self, data):
        insert = Node(data)
        if self.isempty():
            self.tail = insert
        else:
            self.head.previous = insert

        insert.next = self.head
        self.head = insert

    def retrieveend(self):
        returnnode = self.tail
        if self.tail.previous is None:
            self.head = None
        else:
            self.tail.previous.next = None

        self.tail = self.tail.previous
        return returnnode

    def retrievestart(self):
        returnnode = self.head
        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.previous = None

        self.head = self.head.next
        return returnnode
