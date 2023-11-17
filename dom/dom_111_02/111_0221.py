num = int(input())
ans = 0
while num != 0:
    if num %2:
        num //=2
    else:
        num -= 1
    ans += 1

print(ans)