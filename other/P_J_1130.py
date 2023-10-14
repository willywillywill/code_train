

f = [   
        lambda n: True if len([ i for i in range(2, int(n**0.5)+1) if n%i==0 ])==0 else False,
        lambda lst: [ str(i) for i in range(lst[0] if lst[0]>1 else 2,lst[1]+1) if f[0](i) ],
    ]

for i in range(int(input())):
    num = list(map(int, input().split()))
    s = f[1](num)
    for j in s:
        print("".join(j))

