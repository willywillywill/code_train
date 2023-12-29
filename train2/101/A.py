txt = {}
m = input().lower()
while 1:
    s = input().replace(",","").replace(";","").replace(".","")
    if s=="EOF":
        break
    for i in s.split():
        i = i.lower()
        txt[i] = txt.get(i,0)+1
print(f"{txt[m]},{sum(txt.values())}")


"""
the
The villagers of Little Hangleron still called it the Riddle House, even though it had been many 
years since the Riddle family had lived there. It stood on a hill overlooking the village, some of its 
windows boarded, tiles missing from its roof, and ivy spreading unchecked over its face.
EOF
"""