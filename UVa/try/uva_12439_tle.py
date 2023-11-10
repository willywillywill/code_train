import calendar

m,d,y = input().replace(",","").split()
y,d = int(y),int(d)

if (m[0]=="J" and m[1]=="a") or m[0]=="F": y -= 1
t1 = y//400 - y//100 + y//400

m,d,y = input().replace(",","").split()
y,d = int(y),int(d)
if (m[0]=="J" and m[1]=="a") or m[0]=="F": y -= 1
if (m[0]=="F" and d==29): y += 1
t2 = y//400 - y//100 + y//400

print(t2-t1)

"""

2
July 5, 2999
January 5, 3020
June 7, 2999
February 29, 3004


4
1
"""