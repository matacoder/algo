class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def __str__(self):
        return str(self.dataval)


class SLinkedList:
    def __init__(self):
        self.headval = None

    # PUT X
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # SIZE
    def WhatSize(self):
        lngt = 0
        if self.headval is None:
            print(lngt)
            return
        lngt += 1
        laste = self.headval
        while (laste.nextval):
            lngt += 1
            laste = laste.nextval
        print(lngt)

    # PRINT
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    # GET
    def GetRemoveHeadNode(self):
        HeadVal = self.headval
        if (HeadVal is not None):
            print(HeadVal)
            self.headval = HeadVal.nextval
            HeadVal = None
            return
        else:
            print('error')
            return


def engage(object, *args):
    return {
        args[0] == 'get': object.GetRemoveHeadNode,
        args[0] == 'put': object.AtEnd,
        args[0] == 'size': object.WhatSize,
    }[True]



link_list = SLinkedList()
n = int(input())

commands = []
for  i in range(0, n):
    commands.append(input().split(' '))


for command in commands:
    # print(command)
    if len(command) == 1:
        engage(link_list, command[0])()
    else:
        engage(link_list, command[0])(int(command[1]))