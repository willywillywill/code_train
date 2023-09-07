# OK !
while 1:
    n = int(input())
    if not n:
        break

    dp = [0,1]
    while len(dp)<= n+1:
        dp.append(dp[-1]+dp[-2])
    print(dp[-1])