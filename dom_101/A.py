n1 = input().lower()
n = 0
k = 0
l = 0
while 1:
    n2 = list(map(str, input().split()))
    for i in n2:
        if "EOF"==i:
            l = 1
            break

        if "." in i:
            i = i.replace(".","")
        if "," in i:
            i = i.replace(",","")    
        if ";" in i:
            i = i.replace(";","")

        if i.lower()==n1:
            n+=1
        k+=1
    if l:
        break
print("%d,%d"%(n,k))



"""
the
The villagers of Little Hangleron still called it the Riddle House, even though it had been many
years since the Riddle family had lived there. It stood on a hill overlooking the village, some of its
windows boarded, tiles missing from its roof, and ivy spreading unchecked over its face.
EOF

are
Each cell in a Bigtable can contain multiple versions of the same data; these versions are indexed by
timestamp.

Bigtable timestamps are integers.
EOF
"""