lst = list(map(int,input().split()))
m = lst[0]-lst[1]
lst = lst[2:]
lst.sort(reverse=True)
ans = 0
for i in lst:
    if m >= i:
       k = m//i
       ans += k
       m -= k*i
print(ans)


"""
1000 899 50 25 15 10 1 5
"""