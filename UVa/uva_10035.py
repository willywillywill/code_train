
while 1:
    a,b = map(list,input().split())
    if a==b==["0"]:
        break
    
    if len(a)>len(b):
        b = ["0"]*(len(a)-len(b))+b
    elif len(a)<len(b):
        a = ["0"]*(len(b)-len(a))+a
    a = ["0","0"]+a
    b = ["0","0"]+b
    a = a[::-1]
    b = b[::-1]

    ans = 0
    for i in range(len(a)):
        if int(a[i])+int(b[i]) > 9:
            a[i+1] = str(int(a[i+1])+1)
            ans += 1


    print("{} carry operation{}.".format( str(ans) if ans else "No", "s" if ans>1 else ""))