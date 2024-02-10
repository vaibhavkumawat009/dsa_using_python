class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next  = newNode
            self.linkedList.tail= newNode


    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeu(self):
        if self.isEmpty():
            return "there is not any node in the queue"
        else:
            tempNodde = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNodde

    def peek(self):
        if self.isEmpty():
            return "there is not any node in the queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
         
custom  = Queue()
custom.enqueue(1)
custom.enqueue(2)
custom.enqueue(3)
print(custom)
print(custom.dequeu())




