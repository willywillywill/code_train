def dfs(idx):  # 回朔
    global flag

    if flag:
        return
    
    if idx == len(lst):
        if ans[0]==ans[1]==ans[2]:
            flag = True
        return
    
    for i in range(3):
        if ans[i]+lst[idx] <= aver:
            ans[i] += lst[idx]
            dfs(idx+1)
            ans[i] -= lst[idx]
   
flag = False
ans = [0,0,0]
input()
lst = list(map(int,input().split()))
aver = sum(lst)//3

if sum(lst)%3==0:
    dfs(0)
    if flag:
        print("YES")
    else:
        print("NO")
else:
    print("NO")



"""
12 53 34 23 29 26 19 10 1 6
"""