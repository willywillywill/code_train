

while 1:
    try:
        i = input()
        s = [i[0], i[len(i)//2-1:len(i)//2+1] if len(i)%2==0 else i[len(i)//2] ,i[-1]]
        s = [ i.lower() for i in s ]
        print(",".join(s))
    except:
        break
