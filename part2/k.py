class StackMax:
    def __init__(self):
        self.items = []
        self.maximum = [None]
        self.unique = {}

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if str(item) not in self.unique:
            self.unique[str(item)] = 1
            if self.maximum[-1] is not None:
                if int(item) >= self.maximum[-1]:
                    self.maximum.append(int(item))
            else:
                self.maximum.append(int(item))
            self.items.append(item)
        # else:
        #     print(self.unique)

    def pop(self):
        if self.isEmpty() == True:
            print('error')
        else:
            if self.items[-1] == self.maximum[-1]:
                del self.maximum[-1]
            del self.unique[str(self.items[-1])]
            return self.items.pop()

    def peek(self):
        if self.isEmpty() == True:
            print('error')
        else:
            print(self.items[-1])

    def size(self):
            print(len(self.items))

    def get_max(self):
        if self.isEmpty() == True:
            print('None')
        else:
            print(self.maximum[-1])

    def __str__(self):
        output = [str(i) for i in self.items]
        return ' '.join(output)


def engage(object, *args):
    return {
        args[0] == 'get_max': object.get_max,
        args[0] == 'push': object.push,
        args[0] == 'pop': object.pop,
        args[0] == 'size': object.size,
        args[0] == 'peek': object.peek,
    }[True]

stack_max = StackMax()

n = int(input())
commands = []
for  i in range(0, n):
    commands.append(input().split(' '))


for command in commands:
    # print(command)
    if len(command) == 1:
        engage(stack_max, command[0])()
    else:
        engage(stack_max, command[0])(int(command[1]))
    # print(stack_max)

