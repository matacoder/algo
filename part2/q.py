class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0


    def isEmpty(self):
        return self.size == 0

    def push_back(self, x): # Add right + 1
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, x): # Add left - 1
        if self.size != self.max_n:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_back(self): # Delete right - 1
        if self.isEmpty() == True:
            print('error')
        else:
            print(self.queue[self.tail - 1])
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_n
            self.size -= 1

    def pop_front(self): # Delete left + 1
        if self.isEmpty() == True:
            print('error')
        else:
            print(self.queue[self.head])
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1



    def __str__(self):
        output = [str(i) for i in self.queue]
        return ' '.join(output)


def engage(object, *args):
    return {
        args[0] == 'push_back': object.push_back,
        args[0] == 'pop_front': object.pop_front,
        args[0] == 'pop_back': object.pop_back,
        args[0] == 'push_front': object.push_front,
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
    # print(f'HEAD {stack_max.head} : {stack_max.queue[stack_max.head]}. TAIL {stack_max.tail} : {stack_max.queue[stack_max.tail]}')