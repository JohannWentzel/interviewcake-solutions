class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.maxes = Stack()

    def push(self, item):
        if not self.maxes.items:
            self.maxes.push(item)
        elif item >= self.maxes.peek():
            self.maxes.push(item)


        self.stack.push(item)

    def pop(self):
        if self.maxes.peek() == self.stack.peek():
            self.maxes.pop()

        return self.stack.pop()
    def peek(self):
        return self.stack.peek()

    def get_max(self):
        return self.maxes.peek()

if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(1)
    maxStack.push(3)
    maxStack.push(24)
    maxStack.push(22)
    maxStack.push(30)
    maxStack.push(4)
    maxStack.push(2)
    maxStack.push(8)

    maxStack.pop()
    maxStack.pop()
    maxStack.pop()
    maxStack.pop()

    print(maxStack.get_max())
