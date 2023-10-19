def update(n):
    while n<len(bit):
        bit[n]+=1
        n += n&-n
def query(n):
    s = 0
    while n > 0:
        s += bit[n]
        n -= n & -n
    return s


lst = [1,2,3,4,5,6]
bit = [0]*len(lst)

s=0
for i in range(1,len(lst)):
    s += i-query(i)
    update(i)

print(s)