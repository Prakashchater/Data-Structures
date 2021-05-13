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

    def twoSumList(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        sum_list = SinglyLL()

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            # print(s)

            if s >= 10:
                carry = 1
                rem = s % 10
                sum_list.addToList(rem)
            else:
                carry = 0
                sum_list.addToList(s)

            if p:
                p = p.ref
            if q:
                q = q.ref

        sum_list.printLL()

if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addToList(7)
    LL1.addToList(5)
    LL1.addToList(9)
    LL1.addToList(4)
    LL1.addToList(6)
    LL1.printLL()
    print("\n")

    LL2 = SinglyLL()
    LL2.addToList(8)
    LL2.addToList(4)

    LL2.printLL()
    print("\n")

    LL1.twoSumList(LL2)







# Python program to add two numbers represented by linked list

# Node class


# class Node:
#
#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     # Add contents of two linked lists and return the head
#     # node of resultant list
#     def addTwoLists(self, first, second):
#         prev = None
#         temp = None
#         carry = 0
#
#         # While both list exists
#         while (first is not None or second is not None):
#
#             # Calculate the value of next digit in
#             # resultant list
#             # The next digit is sum of following things
#             # (i) Carry
#             # (ii) Next digit of first list (if ther is a
#             # next digit)
#             # (iii) Next digit of second list ( if there
#             # is a next digit)
#             fdata = 0 if first is None else first.data
#             sdata = 0 if second is None else second.data
#             Sum = carry + fdata + sdata
#
#             # update carry for next calculation
#             carry = 1 if Sum >= 10 else 0
#
#             # update sum if it is greater than 10
#             Sum = Sum if Sum < 10 else Sum % 10
#
#             # Create a new node with sum as data
#             temp = Node(Sum)
#
#             # if this is the first node then set it as head
#             # of resultant list
#             if self.head is None:
#                 self.head = temp
#             else:
#                 prev.next = temp
#
#             # Set prev for next insertion
#             prev = temp
#
#             # Move first and second pointers to next nodes
#             if first is not None:
#                 first = first.next
#             if second is not None:
#                 second = second.next
#
#         if carry > 0:
#             temp.next = Node(carry)
#
#     # Utility function to print the linked LinkedList
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, "-->", end=" ")
#             temp = temp.next
#
#
# # Driver code
# first = LinkedList()
# second = LinkedList()
#
# # Create first list
# first.push(6)
# first.push(4)
# first.push(9)
# first.push(5)
# first.push(7)
#
# first.printList()
# print("\n")
# # Create second list
# second.push(4)
# second.push(8)
# second.printList()
# print("\n")
# # Add the two lists and see result
# res = LinkedList()
# res.addTwoLists(first.head, second.head)
#
# res.printList()