w = int(input())
n = int(input())
wl = 0
for i in range(n):
    wi,li = list(map(int,input().split()))
    wl+=wi*li
print(wl//w)
    

"""
29
26
15 5
5 42
15 1
15 27
7 55
7 14
5 5
15 6
5 1
1 2
1 32
7 1
1 1
5 21
1 1
5 1
1 8
1 5
1 28
15 7
1 20
1 1
15 20
1 39
1 3
15 4
"""