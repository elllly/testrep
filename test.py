n, m, f, h = map(int,input().split())
time = list(map(int,input().split()))

priority = []
for i in range(m):
    pair = list(map(int,input().split()))
    priority.append(pair)

emergency = []
for i in range(f):
    pair = list(map(int,input().split()))
    emergency.append(pair)

not_emergency = []
for i in range(h):
    pair = list(map(int,input().split()))
    not_emergency.append(pair)

print(time, priority[0][1], emergency, not_emergency)

to_do_list = [priority[0][0], priority[0][1]]
for i in range(1, m):
    if priority[i][0] in to_do_list:
        to_do_list.append(priority[i][0])