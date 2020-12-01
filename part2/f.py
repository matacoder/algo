# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#
#     def __str__(self):
#         return self.value
#
# def printy(node):
#     print(node)
#     while node.next_item is not None:
#         node = node.next_item
#         print(node)
#     # print(node.next_item)
#
# def solution(node, idx):
#     head = node
#     if idx == 0:
#         # удаляем голову, ставим вместо нее следующий нод
#         head = node.next_item
#         return head
#     while idx:
#         # перемещаемся по нодам до удаляемого
#         if node.next_item is not None:
#             # если следующий есть - старый сохраняем
#             # текущий перезаписываем следующим
#             prev = node
#             node = node.next_item
#         else:
#             # нодов не осталось, уходим
#             break
#         idx -= 1
#     # если мы вышли из цикла раньше чем айди стал 0
#     # то нам дали индекс больший, чем количество элементов
#     if idx != 0:
#         # поэтому вернем голову и все
#         return head
#     if node.next_item is not None:
#         # если следующий элемент есть, то
#         # убиваем наш нод, предыдущему даем ссылку на следующий
#         prev.next_item = node.next_item
#         node = None
#     else:
#         # элемент последний в связанном листе, значит
#         # предыдущий будет ссылать в никуда
#         prev.next_item = None
#     # print(node)
#

def solution(node, idx):
    if not idx:
        return node.next_item
    head = node
    for _ in range(idx):
        try:
            prev_node, node = node, node.next_item
        except Exception:
            return head
    prev_node.next_item = node.next_item
    return head
#
# n = int(input())
# objs = [Node(input()) for i in range(0, n)]
# for i in range(n-1, 0, -1):
#     # print(objs[i])
#     objs[i].next_item = objs[i-1]
#
# solution2(objs[n-1], 116)
# printy(objs[n-1])
