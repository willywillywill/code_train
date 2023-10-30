can = [False]*100001

num = int(input())
data = list(map(int,input().split()))
max_v = sum(data)

can[0] = True
for i in range(num):
    for k in range(max_v,data[i]-1,-1):
        can[k] |= can[k-data[i]]
ans = []
for j in range(1, max_v+1):
    if can[j]:
        ans.append(str(j))
print(len(ans))
print(" ".join(ans))



"""
4
4 2 2 5
"""