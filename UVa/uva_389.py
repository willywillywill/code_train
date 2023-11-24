def to(v,t):
    l = []
    
    while v:
        k = v%t
        
        if k > 9:
            k -= 10
            k = chr(ord("A")+k)
        l.append(str(k))
        v = v//t
    return "".join(l)[::-1]

while 1:
    try:
        v,d,t = input().split()
        v = int(v, int(d))
        l = to(v,int(t))
        if len(l) > 7:
            print("  ERROR")
        elif l:
            print("%7s"%(l))
        else:
            print("%7s"%(v))
    except:
        break

"""
1111000  2 10
1111000  2 16
2102101  3 10
2102101  3 15
  12312  4  2
     1A 15  2
1234567 10 16
   ABCD 16 15
"""