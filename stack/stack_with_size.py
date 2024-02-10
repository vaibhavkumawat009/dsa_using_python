class Stack():
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.copy()
        values.reverse()
        values = [str(x) for x in values]
        return '\n'.join(values)

    # time and space complexity is O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # time and space complexity is O(1)
    def isFull(self):
        if(len(self.list)==self.maxSize):
            return True
        else:
            return False

    # time complexity O(1)/O(n^2)  and space complexity is O(1)
    def push(self,value):
        if(self.isFull()):
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # time and space complexity is O(1)
    def pop(self):
        if self.isEmpty():
            return "There is not an element in the sack"
        else:
            return self.list.pop()

    # time and space complexity is O(1)
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list)-1]

    # time and space complexity is O(1)
    def delete(self):
        self.list = None

customStack = Stack(3)
# print(customStack)
customStack.push(2)
customStack.push(4)
customStack.push(6)
print(customStack.push(8))
print(customStack.peek())
# print(customStack


customStack.push(7)
# print(customStack)
