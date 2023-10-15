#recursion
def f(i):
    n = input()
    out.append(n)
    if i:
        n = input()
        if i-1:
            f(i-1)
        out.append(n)
l = int(input())//2
out = []
f(l)
print(*out)

"""
ab
cd
ef
gh
"""