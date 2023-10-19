def query(n): # bit[i-n] > bit[i] -> sum bit[a,b...]
    s = 0
    while n>0:
        s += bit[n]
        n -= n&-n
    return s

def query(i,j): # bit[i-n] > bit[i] -> sum bit[a,b...]
    s = 0
    while i>=j:
        if i-(i&-i) >= j:
            s += bit[i]
            i -= (i&-i)
        else:
            s += arr[i]
            i -= 1