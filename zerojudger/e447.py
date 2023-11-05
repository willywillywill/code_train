queue = []
for i in range(int(input())):
    n = list(map(int,input().split()))
    if n[0] == 1:
        queue.append(n[1])
    elif n[0] == 2:
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            queue.pop(0)
