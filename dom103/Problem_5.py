fib = [0,1]
st = set()
n = 6
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])

if n not in fib:
    for i in range(2,len(fib)):
        for j in range(2,len(fib)):
            if fib[i]+fib[j] == n and i!=j:
                st.add(tuple(sorted([i,j])))
else:
    print(fib.index(n))
print(st)