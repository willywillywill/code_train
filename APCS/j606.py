k,q,r = map(int,input().split())
ord_str = list(input())
lst = [ord_str.copy()]
for _ in range(q):
    idx = list(map(int,input().split()))
    new_str = [""]*len(idx)
    for i in idx:
        new_str[i-1] = ord_str.pop(0)
    ord_str = new_str
    lst.append(ord_str.copy())
lst = lst[::-1]
for i in range(r):
    for j in range(q-1,-1,-1):
        print(lst[j][i],end=" ")
    print()


"""
4 3 4
abac
4 1 3 2
1 2 3 4
2 3 4 1
"""