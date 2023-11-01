n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
lst.sort()

q1 = (n//4 if n%4==0 else n//4+1)-1
q2 = (n//2 if n%2==0 else n//2+1)-1
q3 = (n*3//4 if n*3%4==0 else n*3//4+1)-1
print("%d,%d,%d"%(lst[q1],lst[q2],lst[q3]))

"""
11 
6 
47 
49 
15 
42 
41 
7 
39 
43 
40 
36

6
15 
7 
36 
41 
40 
39
"""