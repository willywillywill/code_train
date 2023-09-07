
p = lambda x: True if not len([ i for i in range(2,int(x**0.5)+1) if x%i==0 ]) else False

for _ in range(int(input())):
    num = list(map(int, input().split(",")))
    print( "Y" if p(num[0]) and p(num[1]) and (max(num)==min(num)+2)  else "N" )