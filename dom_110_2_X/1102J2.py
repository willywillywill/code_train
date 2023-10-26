# https://www.twblogs.net/a/5cd0bfcbbd9eee6726c905e4
_ = int(input())
lst = list(map(int,input().split()))

p2 = 0
p3 = 0
p5 = 0
ugly = 1
ret = [min(lst)]
while ret[-1] <= max(lst):
    ugly = min([ret[p2]*2, ret[p3]*3, ret[p5]*5])
    ret.append(ugly)
    if ret[p2]*2 == ugly:
        p2 += 1
    if ret[p3]*3 == ugly:
        p3 += 1
    if ret[p5]*5 == ugly:
        p5 += 1
print(ret)
for i in lst:
    print( i in ret )

"""
4
1024 235 450 245
"""