def f(i):
    if i<10: 
        return i
    return f(f(i//10)+i%10)

while 1:
    n = int(input())
    if n==0:
        break
    print(f(n))
"""
while 1:
    n = int(input())
    if not n:
        break
    print(sum([ int(i) for i in str(n) ])%9)    
"""
