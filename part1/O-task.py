server_1 = input().split(' ')
visitors_1 = int(input())
visitors_2 = int(input())
server_2 = input().split(' ')

server_1 = server_1[:visitors_1] + server_2
server_1 = [int(i) for i in server_1]
server_1 = sorted(server_1)
server_1 = [str(i) for i in server_1]
server_1 = ' '.join(server_1)

print(server_1)