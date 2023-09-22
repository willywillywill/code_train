restu = []
for i in range(int(input())):
    num = int(input())
    lst = []
    for i in range(1, num+1):
        if not num %i:
            lst.append(i)
    
    restu.append( "Y" if len(lst)==2 else "N" )

for i in restu:
    print(i)