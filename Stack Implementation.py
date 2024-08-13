"""
STACK
Difficulty : 1/10

Comments : None
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek an empty stack")
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())