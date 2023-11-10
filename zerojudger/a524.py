import itertools

while 1:
    try:
        n = int(input())
        k = list(itertools.permutations("".join(map(str,range(1,n+1))),n))
        for i in k[::-1]:
            print("".join(i))
    except:
        break