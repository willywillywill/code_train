def fun(data):
    i,num = data
    return sum([int(j) for j in str(int(num)*2)]) if i%2 else int(num)


for _ in range(int(input())):
    in1 = input().replace(" ", "")

    in1 = in1[::-1]

    k = list(map(fun, list(enumerate(in1))))
    print( "Valid" if str(sum(k))[-1]=="0" else "Invalid" )

