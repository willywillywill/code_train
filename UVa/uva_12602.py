
for _ in range(int(input())):
    s1,s2 = input().split("-")
    a1,a2 = 0,int(s2)

    s1 = s1[::-1]
    for i in range(len(s1)):
        a1 += (ord(s1[i])-65)*26**i

    if abs(a1-a2) <= 100:
        print("nice")
    else:
        print("not nice")