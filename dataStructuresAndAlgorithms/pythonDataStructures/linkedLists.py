class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insertNewHeader(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def deleteNode(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def deleteTail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
firstChild = Node("Max")
secondChild = Node("Jenny")

family.head.next = wife
wife.next = firstChild
firstChild.next = secondChild

family.insertNewHeader("Dave")

#print(family.search("Bob"))
family.deleteNode("Amy")
family.traversal()
