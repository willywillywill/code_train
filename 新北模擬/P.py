for _ in range(int(input())):
    s = list(map(int,input().split()))
    s1 = s
    for i in range(len(s)):
        t = list(str(s[i]))
        for j in range(len(t)):
            if t[j]!= "9":
                t[j] = "9"
        s[i] = int("".join(t))
        if sorted(s) != s1:
            print("Yes")
            break
    else:
        print("No")

    

"""
3
2020 2020 2020
1 9999999
1 42 4711 9876
"""