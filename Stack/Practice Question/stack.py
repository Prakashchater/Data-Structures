class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return self.data == []

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]

    def getStack(self):
        return self.data

