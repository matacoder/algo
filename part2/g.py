def solution(node, elem):
    # print(node)
    # print(elem)
    # print(elem.value)
    head = node
    i = 0
    if head.value == elem:
        return i
    while True:
        try:
            node = node.next_item
            i += 1
            if node.value == elem:
                return i
        except Exception:
            return -1