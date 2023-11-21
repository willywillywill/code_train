
def dfs(p, s):
    global max_sum
    max_sum = max(max_sum, s)
    for i in mp[p]:
        dfs(i[0], s+i[1])


max_sum = 0
root = input()
mp = {}
for i in range(int(input())):
    a,b,v = input().split()
    if a not in mp:
        mp[a] = []
    if b not in mp:
        mp[b] = []
    mp[a].append([b,int(v)])

dfs(root,0)
print(max_sum)

"""
A
3
A B 2
A C 3
B C 5
"""