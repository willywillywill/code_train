# 1:38

n = int(input())
k = 0
for i in range(1,n+1):
    k+=((-1)**(i+1))/(2*i-1)
print("%.4f"%(4*k))
