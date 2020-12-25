"""
Cпринт 12, Задача А, ревью 2
Матаков Денис
dmatakov@yandex.ru

Задание связано с обратной польской нотацией. Она используется для
парсинга арифметических выражений. Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.

1 дек 2020, 12:15:18
номер успешной посылки 43307457
50ms
3.93Mb
"""
import operator

ACTIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        if self.__items:
            return False
        return True

    def push(self, data):
        self.__items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()


def reverse_poland(sequence):
    """
    Calculate the poland notation
    """
    stack = Stack()

    for item in sequence:
        if item.isnumeric():
            stack.push(item)
        # обрезаем минус для отрицательных чисел
        elif item.startswith('-') and item[1:].isnumeric():
            stack.push(item)
        else:
            try:
                number2, number1 = int(stack.pop()), int(stack.pop())
            except (TypeError, IndexError):
                return f'Stack has not enough elements for operation. Check the sequence!'

            try:
                result = ACTIONS[item](number1, number2)
            except KeyError:
                return f'Operation {item} is not supported.'

            stack.push(result)

    return stack.pop()


if __name__ == "__main__":
    user_input = input().split()
    print(reverse_poland(user_input))
