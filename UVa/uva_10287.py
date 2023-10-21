while 1:
    try:
        n = float(input())

        a1 = n/2*3**0.5
        a2 = 3*n/(3+2*3**0.5)
        a3 = (n/2*3**0.5)/2
        a4 = n*(6*7**0.5-7*3**0.5)/10
        print("%0.10f %0.10f %0.10f %0.10f"%(a1,a2,a3,a4))
    except:
        break