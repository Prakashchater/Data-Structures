class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class SinglyLL:
    def __init__(self):
        self.head = None

    ##Traversal method

    def printLL(self):
        if self.head is None:
            print("Linked List is Empty.!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def addToList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref:
            n = n.ref
        n.ref = new_node

    ##METHOD 1
    # def isPalindrome(self):
    #     p = self.head
    #     s = ""
    #     while p is not None:
    #         s += p.data
    #         p = p.ref
    #     return s == s[::-1]

    ##METHOD 2
    # def isPalindrome(self):
        # p = self.head
        # s = []
        # while p is not None:
        #     s.append(p.data)
        #     p = p.ref
        # p = self.head
        # while p is not None:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.ref
        # return True

    ##METHOD 3
    def isPalindrome(self):
        pass


if __name__ == '__main__':
    LL1 = SinglyLL()

    LL1.addToList("R")
    LL1.addToList("A")
    LL1.addToList("D")
    LL1.addToList("A")
    LL1.addToList("R")

    LL2 = SinglyLL()
    LL2.addToList("C")
    LL2.addToList("B")
    LL2.addToList("A")

    print(LL1.isPalindrome())
    print(LL2.isPalindrome())
