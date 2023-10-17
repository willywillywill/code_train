n = 5

print(*[ i for i in range(n) ])
for j in range(1,n-1):
    print(*[ abs(i-j) if (i==0 or i==n-1) else " " for i in range(n) ])
print(*[ i for i in range(n) ][::-1])
