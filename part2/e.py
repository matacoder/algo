# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#
#     def __str__(self):
#         return self.value


def solution(node):
    print(node)
    while node.next_item is not None:
        node = node.next_item
        print(node)


# s3 = Node('3')
# s2 = Node('2', s3)
# s1 = Node('1', s2)
#
#
#
#
# solution(s1)