def h(i,l):
    k = sum([ int(j)**2 for j in str(i)])
    if k in l:
        return 0
    elif k==1:
        return 1
    else:
        l.append(k)
        return h(k,l.copy())
for i in range(int(input())):
    n = int(input())
    if h(n,[]):
        print("Case #%d: %d is a Happy number."%(i+1,n))
    else:
        print("Case #%d: %d is an Unhappy number."%(i+1,n))
