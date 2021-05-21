# Time : O(N)     SPACE: O(1)

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
                print(n.data,"-->", end=" ")
                n = n.ref

    ##ADD IN BEGINNING

    def addBegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    ##AT THE END
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def reverse(self, head):
        curr = head
        prev = None

        while curr is not None:
            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt
        head = prev
        return head


    def addOne(self, head):
        head = self.reverse(head)
        curr = head
        while curr is not None:
            if curr.data == 9 and curr.ref is None:
                curr.data = 1
                new_node = Node(0)
                new_node.ref = head
                head = new_node
                curr = curr.ref
            elif curr.data == 9:
                curr.data = 0
                curr = curr.ref
            else:
                curr.data = curr.data + 1
                curr = curr.ref
                break

        head = self.reverse(head)
        return head


if __name__ == '__main__':

    LL1 = SinglyLL()
    LL1.addBegin(9)
    LL1.addBegin(9)
    LL1.addBegin(9)
    LL1.addBegin(9)
    LL1.addBegin(1)
    head = LL1.addOne(LL1.head)
    LL1.printLL()