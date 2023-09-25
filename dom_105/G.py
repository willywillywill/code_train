for _ in range(int(input())):
    s1 = input().strip()
    s2 = input().strip()

    lst = [[0 for j in range(len(s1))] for i in range(len(s2))]
    for i in range(1,len(s2)):
        for j in range(1,len(s1)):
            if s2[i]==s1[j]:
                lst[i][j] = lst[i-1][j-1]+1
            else:
                lst[i][j] = max(lst[i-1][j], lst[i][j-1])
    
    if len(s1) == len(s2):
        print(lst[-1][-1])
    else:
        print(lst[-1][-1]+1)

"""
2
ACCGATGCAGCGCTC
CCGATGA
abcdghxy
aedfhrz

2
13567
24680
ab12
Abc1
"""