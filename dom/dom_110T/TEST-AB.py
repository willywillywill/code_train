for _ in range(int(input())):
    A = 0
    B = 0
    s1,s2 = map(list,input().split(","))
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            A += 1
        elif s2[i] in s1:
            B += 1
    print(f"{A}A{B}B")