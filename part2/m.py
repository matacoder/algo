class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0


    def isEmpty(self):
        return self.size == 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def get(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop(self):
        if self.isEmpty() == True:
            print('None')
        else:
            print(self.queue[self.head])
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1

    def peek(self):
        if self.isEmpty() == True:
            print('None')
        else:
            print(self.queue[self.head])


    def __str__(self):
        output = [str(i) for i in self.queue]
        return ' '.join(output)


def engage(object, *args):
    return {
        args[0] == 'push': object.put,
        args[0] == 'pop': object.pop,
        args[0] == 'size': object.size,
        args[0] == 'peek': object.peek,
    }[True]



n = int(input())
max_size = int(input())
stack_max = MyQueue(max_size)

commands = []
for  i in range(0, n):
    commands.append(input().split(' '))


for command in commands:
    # print(command)
    if len(command) == 1:
        if command[0] == 'size':
            print(stack_max.size)
        else:
            engage(stack_max, command[0])()
    else:
        engage(stack_max, command[0])(int(command[1]))
    # print(stack_max)