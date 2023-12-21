for _ in range(int(input())):
    n = int(input())
    ans = set()
    s = list(input())
    for i in range(len(s)-1):
        s1 = s.copy()
        for j in range(i, i+2):
            s1[j] = ""
        rst = "".join(s1)
        ans.add(rst)
    print(len(ans))