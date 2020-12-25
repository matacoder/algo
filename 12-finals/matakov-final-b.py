"""
Cпринт 12, Задача B
Матаков Денис
dmatakov@yandex.ru

В качестве второго задания финального проекта нужно
написать программу, которая определяет, есть ли цикл
в связном списке.

1 дек 2020, 13:06:35
номер успешной посылки 43308491
52ms => 41ms
5.86Mb => 5.53Mb
"""


def hasCycle(head):
    """
    Floyd's Cycle-Finding Algorithm
    :param head: головной элемент
    :return: булево значение
    """

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            return True
    return False
