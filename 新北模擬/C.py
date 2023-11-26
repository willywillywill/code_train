def f(s):
    return s[0],s[1],s[2]

lst = []
for _ in range(int(input())):
    lst.append(input().split("^"))
lst.sort(key=f)

"""
4
2^2^2
3^4
15
9^2
"""