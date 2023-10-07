
def MMS(i,n):
    if i==0:
        return n
    if lst[i-1] > n+lst[i-1]:
        MMS(i-1,lst[i-1])
    else:
        MMS(i-1, lst[i-1]+n)
    


lst = list(map(int,"-2 -3 4".split()))
print(MMS(len(lst), 0))