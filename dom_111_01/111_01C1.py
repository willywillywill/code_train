n = 2**15
premi = [1] *(n+1)
for i in range(2, int(n**0.5)+1):
    if premi[i]:
        for j in range(i*i, n+1, i): # 倍數 2,3 ... 
            premi[j] = 0

premi = [ i for i in range(2, n+1) if premi[i] ]


while 1:
    in1 = int(input())
    if not in1:
        break
    st = set()
    for i in range(2,in1):
        for j in range(2,in1):
            if i in premi and j in premi and i+j==in1 and (j,i) not in st:
                st.add((i,j))
    print(len(st))
"""
8
20
42
10
12
4
0
"""