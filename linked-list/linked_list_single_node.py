class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


# linked list for only one node which head and tail point to the same node
class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


node1 = LinkedList(40)
print(node1.tail.value)
