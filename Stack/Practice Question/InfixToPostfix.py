# from stack import Stack

class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.data = []
        self.output = []
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return self.data == []

    def peek(self):
        return self.data[-1]

    def push(self, op):
        self.top += 1
        self.data.append(op)

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.data.pop()
        else:
            return "$"

    # A utility function to check is the given character is operand
    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.operators[i]
            b = self.operators[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if ((not self.isEmpty()) and (self.peek() != '(')):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.output.append(self.pop())
        print("".join(self.output))

if __name__ == '__main__':
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    obj = Conversion(len(exp))
    obj.infixToPostfix(exp)

