while 1:
    try:
        n = int(input())
        n = ((n+1)*((n*n)-n+6))//6
        print(n)
    except:
        break