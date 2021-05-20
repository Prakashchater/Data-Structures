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

    ##ADD AFTER A NODE
    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    ##ADD BEFORE NODE
    def before_node(self, data, x):
        if self.head is None:
            print("Linked list is Empty!.")
            return
        if x == self.head.data:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present in the Linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    ##TIME = O(N)   SPACE=O(N)
    ##USINH HASHING
    # def detectLoop(self, head):
    #     s = set()
    #     curr = head
    #     if curr in s:
    #         return True
    #     s.add(curr)
    #     curr = curr.next
    #     return False



    ##TIME = O(N)   SPACE = O(1)
    ##USING FLOYD'S ALGORITHM
    def detectLoop(self, head):
        slow = head
        fast = head
        while slow and fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addBegin(20)
    LL1.addBegin(10)
    LL1.add_end(30)
    LL1.printLL()


