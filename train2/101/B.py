txt = {}
while 1:
    s = input()
    if s == "EOF":
        break
    for i in s.split():
        i = i.lower()
        txt[i] = txt.get(i,0)+1
txt = list(txt.items())
txt.sort(key=lambda x:x[1], reverse=True)
ans = []
for i in range(3):
    ans.append(str(txt[i][1]))
print(",".join(ans))
"""
Google Google Google Google Google Linux Linux Linux Linux Google Google Google Google 
Google Web Analysis SEO SEO SEO SEO Windows Windows Windows Windows Yahoo Yahoo 
Time time yahoo Yahoo
EOF
"""