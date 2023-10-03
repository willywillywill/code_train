hash_f = lambda l,r: ((hash_table[r]-hash_table[l-1]*p**(r-l+1))%mod+mod)%mod
p = 7
mod = 91

while 1:
    s = input().strip()
    if s==".":
        break
    s_idx = list(set(s))
    idx = {}
    for i in range(len(s_idx)):
        idx[s_idx[i]] = i+1
    L = len(s)
    x = [ i for i in range(1, L) if L%i==0 ]
    hash_table = [0]*L
    for i in range(L):
        hash_table[i] = ((hash_table[i-1] if i else 0)*p+idx[s[i]])%mod
    out = []
    for i in x:
        for j in range(int(L/i)):
            r = i*(j+1)-1
            l = j*i
            c = 0
            if hash_f(l,r) in hash_table:
                c = int(L/i)
        if c:
            out.append(c)

    if out:
        print(max(out))
    else:
        print(1)

"""
ABCD
AAAA
ababab
.
"""