class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.size += 1
        return self.data.append(item)


    def pop(self):
        self.size -= 1
        return self.data.pop()

def reverseString(s, inp):

    for i in range(len(inp)):
        s.push(inp[i])

    rev_str = ""
    while not s.isEmpty():
        rev_str += s.pop()
    return rev_str

if __name__ == '__main__':
    s = Stack()
    inp_str = input("Enter a word: ")
    print(reverseString(s, inp_str))
    print(s.getSize())



