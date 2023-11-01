num = int(input())
data = list(map(int,input().split()))
ans = 0
data.sort()
while len(data) > 1:
    t = data.pop(0)+data.pop(0)
    data.append(t)
    ans += t
    data.sort()

print(ans)

"""
61
2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 5 61 63 65

"""