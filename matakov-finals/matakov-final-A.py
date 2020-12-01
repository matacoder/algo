"""
Cпринт 12, Задача А, ревью 2
Матаков Денис
dmatakov@yandex.ru

Задание связано с обратной польской нотацией. Она используется для
парсинга арифметических выражений. Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.

1 дек 2020, 12:15:18
номер успешной посылки 43169379
49ms
3.97Mb
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
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


def main():
    user_input = input().split()
    stack = Stack()

    for item in user_input:
        if item.isnumeric():
            stack.push(item)
        # обрезаем минус для отрицательных чисел
        elif item.startswith('-') and item[1:].isnumeric():
            stack.push(item)
        else:
            number2, number1 = int(stack.pop()), int(stack.pop())
            result = ACTIONS[item](number1, number2)
            stack.push(result)

    return stack.pop()


if __name__ == "__main__":
    print(main())
