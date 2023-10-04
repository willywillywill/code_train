hash_f = lambda l,r: ((hash_table[r]-hash_table[l-1]*p**(r-l+1))%mod+mod)%mod
chick = lambda l,r,x: hash_f(l,r) == hash_table[x-1]
p = 7
mod = 91


s = "aaaa"
 
s_idx = list(set(s))
idx = {}
for i in range(len(s_idx)):
    idx[s_idx[i]] = i+1
L = len(s)
x = [ i for i in range(1, L) if L%i==0 ]
hash_table = [0]*L
for i in range(L):
    hash_table[i] = ((hash_table[i-1] if i else 0)*p+idx[s[i]])%mod
print(hash_table)

for i in x:
    for j in range(1, int(L/i)):
        



"""
ABCD
AAAA
ababab
.
"""