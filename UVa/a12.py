

while 1:
    try:
        n1, n2 = list(map(int, input().split()))
        print(abs(n1-n2))
    except:
        break