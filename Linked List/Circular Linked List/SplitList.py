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


if __name__ == '__main__':
    cLL = CircularLL()
    cLL.prepend("B")
    cLL.prepend("A")
    cLL.append("C")
    cLL.append("D")
    cLL.append("E")
    cLL.append("F")
    cLL.append("G")
    # cLL.printCLL()
    cLL.splitList()
    # print(len(cLL))