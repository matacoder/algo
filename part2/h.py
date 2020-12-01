def solution(node):
    temp = None
    current = node

    # Swap next and prev for all nodes of
    # doubly linked list
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        head = current
        current = current.prev

    # Before changing head, check for the cases like
    # empty list and list with only one node
    if temp is not None:
        head = temp.prev
    return head