

num = 0
ans = 0
while 1:
    n = int(input())
    if n==-9999:
        break
    
    num += n
    if num < 0:
        num = 0
    ans = max(num,ans)
print(ans)