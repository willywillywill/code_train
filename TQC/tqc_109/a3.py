# 5:32
# 2:41

n = int(input())
def f(i):
    if i==2:
        return 1/((i-1)**0.5+i**0.5)
    return f(i-1)+(1/((i-1)**0.5+i**0.5))
print("%.4f"%(f(n)))