class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def delete_node(head, del_):
    #Empty LL
    if head == None or del_ == None:
        return None
    #if head is to be deleted
    if head == del_:
        head = del_.next

    # Change next only if node to be deleted
    # is NOT the last node
    if del_.next != None:
        del_.next.prev = del_.prev

    # Change prev only if node to be deleted
    # is NOT the first node
    if del_.prev != None:
        del_.prev.next = del_.next

    return head

##REMOVE DUPLICATE
def removeDuplicates(head):
    if head is None:
        return None

    # unordered_set 'us' implemented as hash table
    seen = set()

    curr = head
    nxt = None

    while curr is not None:
        if curr.data in seen:
            nxt = curr.next

            head = delete_node(head, curr)

            curr = nxt
        else:
            seen.add(curr.data)
            curr = curr.next
    return head

def push(head, data):
    new_node = Node(data)
    new_node.prev = None
    new_node.next = head
    if head != None:
        head.prev = new_node

    head = new_node
    return head

def printLL(head):
    if head == None:
        print("DLL is empty.")

    while head != None:
        print(head.data, "-->", end=" ")
        head = head.next


head = None

# Create the doubly linked list:
# 8<->4<->4<->6<->4<->8<->4<->10<->12<->12
head = push(head, 12)
head = push(head, 12)
head = push(head, 10)
head = push(head, 4)
head = push(head, 8)
head = push(head, 4)
head = push(head, 6)
head = push(head, 4)
head = push(head, 4)
head = push(head, 8)
print("Original Doubly linked list:")
printLL(head)
head = removeDuplicates(head)
print("\nDoubly linked list after removing duplicates:")
printLL(head)


