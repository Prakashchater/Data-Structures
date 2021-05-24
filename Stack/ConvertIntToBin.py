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

def convertIntegerToBinary(s, num):
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    bin_num = ""
    while not s.isEmpty():
        bin_num += str(s.pop())
    return bin_num

s = Stack()
n = int(input("Enter a number: "))
print(convertIntegerToBinary(s, n))
