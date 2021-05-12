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
    # def count_occurance(self, x):
    #     count = 0
    #     curr = self.head
    #     while curr:
    #         if x == curr.data:
    #             count += 1
    #         curr = curr.ref
    #     return count


##RECURSIVE WAY
    def count_occurance(self,node,x):
        if not node:
            return 0
        if node.data == x:
            return 1 + self.count_occurance(node.ref, x)
        else:
            return self.count_occurance(node.ref, x)


if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addToList(1)
    LL1.addToList(2)
    LL1.addToList(1)
    LL1.addToList(2)
    LL1.addToList(1)
    LL1.addToList(2)
    LL1.addToList(3)
    LL1.addToList(1)
    print(LL1.count_occurance(LL1.head,2))
