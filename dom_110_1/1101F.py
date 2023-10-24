
for _ in range(int(input())):
    n1 = input()
    n2 = input()
    ans = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            ans += 1
    print(ans)