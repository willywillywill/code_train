dit = {}
l=0
while 1:
    n2 = list(map(str, input().split()))
    for i in n2:
        i = i.lower()
        if "eof"==i:
            l=1
            break
        dit[i] = dit.get(i, 0)+1
    if l:
        break

lst = list(dit.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(3):
    print(lst[i][1], end="," if i!=2 else "")


"""
Google Google Google Google Google Bible Bible Bible Bible Google Google Google Google
Google Bible Bible Bible Bible Website Analysis

SEO SEO SEO SEO SEO SEO SEO Quality Windows Windows Windows Yahoo Yahoo Word
Word Yahoo
EOF

Google Google Google Google Google Linux Linux Linux Linux Google Google Google Google
Google Web Analysis SEO SEO SEO SEO Windows Windows Windows Windows Yahoo Yahoo
Time time yahoo Yahoo
EOF
"""