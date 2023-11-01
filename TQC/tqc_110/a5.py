lst = list(map(str,input().split(',')))
lst = [ [ int(j) for j in i] for i in lst]
max_sum = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][j] in (1,2):
            for k in range(i,len(lst)):
                for l in range(j, len(lst)):
                    n = [ lst[xx][yy] for xx in range(i,k+1) for yy in range(j,l+1) ]
                    if all([ m in (1,2)for m in n]):
                        sub_lst_sum = sum(n)
                        max_sum = max(max_sum, sub_lst_sum)             
print(max_sum)
"""
02012,01100,20211,00120
"""