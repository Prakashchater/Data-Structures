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


##MERGING TWO SORTED
# def merge_two_sorted(head1, head2):
#     temp = Node(0)
#     tail = temp
#     while True:
#         if head1 is None:
#             tail.ref = head2
#             break
#         if head2 is None:
#             tail.ref = head1
#             break
#
#         if head1.data <= head2.data:
#             tail.ref = head1
#             head1 = head1.ref
#         else:
#             tail.ref = head2
#             head2 = head2.ref
#
#         tail = tail.ref
#     return temp.ref

##USING RECURSION
def merge_two_sorted(head1, head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.ref = merge_two_sorted(head1.ref, head2)
    else:
        temp = head2
        temp.ref = merge_two_sorted(head1, head2.ref)

    return temp


LL1 = SinglyLL()
LL2 = SinglyLL()

LL1.addToList(1)
LL1.addToList(30)
LL1.addToList(55)

LL2.addToList(2)
LL2.addToList(4)
LL2.addToList(60)

LL1.head = merge_two_sorted(LL1.head, LL2.head)

LL1.printLL()
