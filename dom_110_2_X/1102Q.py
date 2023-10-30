n = int(input())
lst = list(map(int,input().split()))
ans = []
while len(lst) > 1:
    lst.sort()
    a1 = lst.pop(0)
    a2 = lst.pop(0)
    lst.append(a1+a2)
    ans.append(a1+a2)
print(ans)
print(sum(ans))
print(lst)

"""
3
1 2 9

9
2 4 5 6 7 8 9 11 13

61
2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 5 61 63 65

"""