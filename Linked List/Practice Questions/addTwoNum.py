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

    # Input:
    # List1: 5->6->3 // represents number 365
    # List2: 8->4->2 // represents number 248
    # Output: Resultant
    # list: 3->1->6 // represents number 613
    # Explanation: 365 + 248 = 613
    ##WHEN THE LINKED LIST IS ALREADY REVERSED

    def addTwo(self, first, second):
        temp = None
        curr = None
        res = None
        carry = 0
        s = 0

        while first is not None or second is not None:
            f_data = 0 if first is None else first.data
            s_data = 0 if second is None else second.data
            s = carry + f_data + s_data

            carry = 1 if s >= 10 else 0
            s = s if s < 10 else s % 10

            temp = Node(s)

            if self.head is None:
                self.head = temp
            else:
                curr.ref = temp

            curr = temp

            if first is not None:
                first = first.ref

            if second is not None:
                second = second.ref

        if carry > 0:
            temp.ref = Node(carry)



##GFG SOLUTION
"""
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt
        head = prev
        return head


    def addTwoLL(self, first, second):
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        s = 0
        temp = curr = res = None
        while first is not None or second is not None:
            f_data = 0 if first is None else first.data
            s_data = 0 if second is None else second.data
            s = carry + f_data + s_data

            c = 1 if s >= 10 else 0
            s = s if s < 10 else s % 10
            temp = Node(s)

            if res is None:
                res = temp
            else:
                curr.ref = temp
            curr = temp

            if first :
                first = first.ref

            if second:
                second = second.ref

        if carry > 0:
            temp = Node(carry)
            curr.ref = temp
            curr = temp

        res = self.reverse(res)
        return res
"""





if __name__ == '__main__':
    LL1 = SinglyLL()
    LL2 = SinglyLL()
    LL1.addBegin(3)
    LL1.addBegin(4)
    LL1.addBegin(5)
    LL1.printLL()
    print("\n")
    LL2.addBegin(4)
    LL2.addBegin(5)
    LL2.printLL()
    print("\n")

    res = SinglyLL()
    res.addTwo(LL1.head, LL2.head)
    res.printLL()




