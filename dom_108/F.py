in1 = list(map(int,"1 6".split()))
lst = []
out = []
while 1:
    out.append(in1[0]//in1[1])
    s = in1[0]%in1[1]
    in1[0] = s*10
    if s in lst:
        lst.append(s)
        break
    lst.append(s)
if lst[-1]==lst[-2]:
    print(out[0],end=".")
    for i in range(1,len(out)-1):
        print(out[i],end="")
    print("(%d)"%(out[-1]))
else:
    print(out[0],end=".")
    print("(",end="")
    for i in range(1,len(out)):
        print(out[i],end="")
    print(")")
    


"""
1 / 6 = 0.166666... = 0.1(6) 
[0, 1, 6]
[1, 4, 4]

5 / 7 = 0.714285714285.... = 0.(714285)
[0, 7, 1, 4, 2, 8, 5]
[5, 1, 3, 2, 6, 4, 5]

1 / 250 = 0.004 = 0.004(0), 由於沒有循環小數溆炻廠出(0)
[0, 0, 0, 4, 0]
[1, 10, 100, 0, 0]
"""