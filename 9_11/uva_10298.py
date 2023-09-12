
while True:
    s=input()
    if s==".":
        break
    l=len(s)
    if s==s[::-1]: #ex."AAAA"
        print(l)
        continue

    factor=[ i for i in range(2,l) if l%i==0 ] #因數位

    for fac in factor:
        idx=s[0:fac]
        k=l//fac #倍數
        if idx*k==s: #ex."AB"*3 = "ABABAB"
            print(k)
            break
    else:
        print(1)