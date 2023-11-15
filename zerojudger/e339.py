"""
sum(lst[:i+1]) -> error every times 
s += lst[i]    -> ok    1
"""

input()
lst = list(map(int,input().split()))
s = 0
for i in range(len(lst)):
    s += lst[i]
    print(s, end=" ")
print()

