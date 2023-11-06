lst = list(map(int,input().split(",")))
n = lst[0]
lst = lst[1:]
count = [30,18,8,5,1,50,1,10,4,1]
lst = [ [lst[i],count[i]] for i in range(10) ]
lst.sort(key=lambda x:x[0],reverse=True)

for i in range(len(lst)):
    for j in range(len(lst)):
        



"""
3,200,1,1,1,1,1,1,1,1,1,1 
"""