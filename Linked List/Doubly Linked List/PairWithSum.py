class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

    # ##FORWARD TRAVERSAL
    # def forward_printLL(self):
    #     if self.head is None:
    #         print("Linked list is empty!.")
    #     else:
    #         n = self.head
    #         while n is not None:
    #             print(n.data, "-->", end=" ")
    #             n = n.nref

 ##INSERT AT THE BEGINNING
def add_begin(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.nref = head
        head.pref = new_node
        head = new_node
    return head

def pair_with_sum(head, sum_val):
    first = head
    second = head
    pairs = list()

    while second.nref is not None:
        second = second.nref

    found = False

    while first != second and second.nref != first:
        if first.data + second.data == sum_val:
            found = True
            print("(", first.data, ",", second.data, ")")
            first = first.nref
            second = second.pref
        else:
            if first.data + second.data < sum_val:
                first = first.nref
            else:
                second = second.pref
    if found == False:
        print("No pair found.")


if __name__ == '__main__':
    head = None
    head = add_begin(head, 5)
    head = add_begin(head, 4)
    head = add_begin(head, 3)
    head = add_begin(head, 2)
    head = add_begin(head, 1)
    sum_val = 5
    pair_with_sum(head, sum_val)


