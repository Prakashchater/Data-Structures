"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def printCLL(self):
        if self.head is None:
            print("Circular Linked list is empty.")
        else:
            curr = self.head
            while curr:
                print(curr.data, "-->", end=" ")
                curr = curr.next
                if curr == self.head:
                    break

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            curr = self.head
            new_node = Node(data)
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def splitList(self):
        size = len(self)    #Len function is used to calculate the length of the list.
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0
        curr = self.head
        prev = None
        ## this is for the first split
        while curr is not None and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        prev.next = self.head
        ##This is for second split
        split_list = CircularLL()
        while curr.next != self.head:
            split_list.append(curr.data)
            curr = curr.next
        split_list.append(curr.data)

        print("First Node: ")
        self.printCLL()
        print("\nSecond Node: ")
        split_list.printCLL()
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def printCLL(self):
        if self.head is None:
            print("CLL is Empty.")
        else:
            curr = self.head
            while curr:
                print(curr.data, "-->", end=" ")
                curr = curr.next
                if curr == self.head:
                    break

    def push(self, data):
        curr = self.head
        new_node = Node(data)

        new_node.next = self.head
        if self.head is not None:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    #Split two list with Floyd's Algo(Tortoise and Hare algorithm)
    def split_list(self, head1, head2):
        #Make a two pointers
        fast = self.head
        slow = self.head

        if self.head is None:
            return
        #If the list is even then we have to move the fast --> fast.next.next and slow --> slow.next
        while fast.next != self.head and fast.next.next != self.head:
            fast = fast.next.next
            slow = slow.next

        #If there are even elements in the list then move fast
        if fast.next.next == self.head:
            fast = fast.next

        #Set the Head pointer to first half
        head1.head = self.head

        # Set the head pointer of second half
        if self.head.next != self.head:
            head2.head = slow.next

        #Make the first half
        fast.next = slow.next

        #Make the second half
        slow.next = self.head

if __name__ == '__main__':
    cLL = CircularLL()
    head1 = CircularLL()
    head2 = CircularLL()
    cLL.push(6)
    cLL.push(5)
    cLL.push(4)
    cLL.push(3)
    cLL.push(2)
    cLL.push(1)
    print("Original CLL:")
    cLL.printCLL()

    cLL.split_list(head1, head2)

    print("\nFirst CLL:")
    head1.printCLL()

    print("\nSecond CLL: ")
    head2.printCLL()
