s = list(map(int, input().replace(" ",",").split(","))) 
num = s.pop(-1)
k = -1
for i in range(len(s)):
    if s[i] >= num:
        k = i
        break
if k < 0:
    print(len(s))
else:
    print(k)

"""
1,3,5,6 5
"""