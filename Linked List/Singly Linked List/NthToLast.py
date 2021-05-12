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

    ##ITERATIVE WAY
    # def iterative_nth_to_last(self, n):
    #     curr = self.head
    #     count = 0
    #     while curr:
    #         if count == n:
    #             return curr.data
    #         count += 1
    #         curr = curr.ref
    #     assert(False)
    #     return 0

    ##RECURSIVE WAY
    def get_nth(self, llist, pos):
        llist.get_nth_node(self.head, pos, llist)

    def get_nth_node(self, head, pos, llist):
        count = 0
        if head is not None:
            if count == pos:
                print(head.data)
            else:
                llist.get_nth_node(head.ref, pos - 1, llist)
        else:
            print("Index not present.")


LL1 = SinglyLL()
LL1.addToList("A")
LL1.addToList("B")
LL1.addToList("C")
LL1.addToList("D")
LL1.addToList("E")

# print(LL1.calculate_length())
# print(LL1.nth_to_last(0))
LL1.get_nth(LL1, 4)
# LL1.printLL()
