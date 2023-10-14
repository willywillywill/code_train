"""
for _ in range(int(input())):

    str1 = input().replace(" ","")

    lst1 = [ str(int(str1[i])*2) for i in range(0,len(str1),2) ]
    lst2 = [ int(str1[i]) for i in range(len(str1)) if i%2]
    
    lst1 = [ int(i[0])+int(i[1]) if len(i)==2 else int(i) for i in lst1 ]

    lst1 = sum(lst1)
    lst2 = sum(lst2)

    print( 'Valid' if (lst1+lst2)%10==0 else 'Invalid')
"""

from sys import stdin,stdout
m = dict(zip("0123456789", map(int,"0246813579")))
li = {
        s:( m[s[0]]+m[s[2]]+int(s[1])+int(s[3]) )%10 
        for s in [f'{k:04}'for k in range(10000)]
    }
next(stdin)
stdout.writelines(
    "Invalid\n"
    if sum(li[k] for k in line.split())%10 
    else "Valid\n" 
    for line in stdin.readlines()
)
