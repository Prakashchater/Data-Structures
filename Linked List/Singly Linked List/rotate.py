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

    def calculate_length(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.ref
        return count

    def rotateLL(self, k):
        p = q = self.head
        prev = None
        count = 0
        while p is not None and count < k:
            prev = p
            p = p.ref
            q = q.ref
            count += 1
        p = prev
        while q is not None:
            prev = q
            q = q.ref
        q = prev
        q.ref = self.head
        self.head = p.ref
        p.ref = None

if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addToList(1)
    LL1.addToList(2)
    LL1.addToList(3)
    LL1.addToList(4)
    LL1.addToList(5)
    LL1.addToList(6)
    LL1.printLL()
    print("\n")
    LL1.rotateLL(3)
    LL1.printLL()

