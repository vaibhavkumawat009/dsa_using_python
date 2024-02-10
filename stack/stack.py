class Stack():
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.copy()
        values.reverse()
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "Element added to the stack"

    def pop(self):
        if(self.isEmpty()):
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if(self.isEmpty()):
            return "Stack is empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)
print(customStack.pop(),"poped element")


print(customStack)

print('\n')
print(customStack.isEmpty())
