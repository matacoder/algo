"""
Cпринт 12, Задача B
Матаков Денис
dmatakov@yandex.ru

В качестве второго задания финального проекта нужно
написать программу, которая определяет, есть ли цикл
в связном списке.

1 дек 2020, 13:06:35
номер успешной посылки 43173516
52ms
5.86Mb
"""


def hasCycle(head):
    """
    Floyd's Cycle-Finding Algorithm
    :param element: головной элемент
    :return: булево значение
    """

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            return True
    return False
