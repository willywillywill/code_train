


def query(n):
    s = 0
    while len(lst)>n>0:
        s += bit[n]
        n -= n&-n
    return s
def update(n):
    while n<len(lst):
        bit[n]+=lst[n]
        n += n&-n

lst = [5,2,3,4,1]
bit = [0]*len(lst)
ans = 0
for i in range(len(lst)):
    ans += i-query(lst[i])
    update(lst[i])
print(ans)

"""
5 4
4 5
2 4
2 5
2 2
"""