for _ in range(int(input())):
    input()
    m,n = map(int,input().split())
    lst = []
    for i in range(n):
        s = input()
        a = 0
        for i in range(m):
            for j in range(i+1,m):
                if s[i] > s[j]:
                    a += 1
        lst.append([a,s])

    lst.sort(key=lambda x:x[0])
    for i in lst:
        print(i[1])

"""
10 6
AACATGAAGG
TTTTGGCCAA
TTTGGCCAAA
GATCAGATTT
CCCGGGGGGA
ATCGATGCAT
"""