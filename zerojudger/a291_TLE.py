import sys

try:
    for i in sys.stdin:
        ans = list(map(int,i.split()))
        for _ in range(int(input())):
            a = ans.copy()
            use = list(map(int,input().split()))
            A = 0
            B = 0
            for j in range(len(use)):
                if a[j] == use[j]:
                    a[j] = -1
                    use[j] = -1
                    A += 1
            for j in range(len(a)):
                if use[j] != -1:
                    if use[j] in a:
                        B += 1
            print("%dA%dB"%(A,B))
except:
    pass

"""

1 2 3 4
4
1 1 4 5
1 2 4 3
1 1 4 4
4 3 2 1

1 1 1 5
4
1 1 1 1
0 9 2 8
1 5 2 3
1 1 5 1
"""