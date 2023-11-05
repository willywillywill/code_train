for _ in range(int(input())):
        s = list(map(int,input()))
        ans = 1
        for i in s:
            ans *= i
        print(ans)