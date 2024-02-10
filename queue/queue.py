class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True

        else:
            return False

    def enqueue(self,value):
        self.items.append(value)
        return "Element is added successfully"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

customeQueue = Queue()
customeQueue.enqueue(1)
customeQueue.enqueue(2)
customeQueue.enqueue(3)
customeQueue.dequeue()
print(customeQueue.peek())
print(customeQueue)