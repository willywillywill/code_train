for _ in range(int(input())):
    m,n,q = list(map(int,input().split()))
    arr = []
    sch = []

    for _ in range(m):
        arr.append(list(input()))
    for _ in range(q):
        sch.append(list(map(int,input().split())))

    print(m,n,q)
    for x,y in sch:
        add = 1
        run = True
        while run:
            tx,bx = x-add,x+add
            ly,ry = y-add,y+add
            if tx<0 or ly<0 or bx>=m or ry>=n:
                break

            for i in range(tx,bx+1):
                if arr[i][ly:ry+1] != [arr[x][y]]*(ry-ly+1):
                    run = False
                    break
            else:
                add+=1
        print(ry-ly-1)

"""
7
7 10 5
abbbabaaaa
abbbaaaaaa
abbbbaaaaa
baabbaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
6 3
4 7
1 1 1
a
0 0
0 0 0
5 5 3
AAAAA
ABABA
ABABA
ABABA
AAAAA
2 2
0 0
1 1
20 30 5
111111111222222222333333311111
111111111112222233333311111444
111222111111122222222222111133
222222222222222222222222222222
333333312222222221111111111111
333333333332222222222222211111
333333311112222224444411111111
333333333332222244444411111111
333333311112222244444444444444
333333333322222224444444444443
333333333332222244444411111111
333333311112222244444444444444
333333333322222224444444444443
111111111111111111111111111111
111111111111111111111111111122
111111333311111111111111111122
111111333311111333333333333333
111111333311111111111111111111
111111333311111111111111111111
111111333311111111111111111111
1 1
8 3
17 8
7 20
5 13
9 10 1
qqqqqqqqqW
UUUUqqqqqK
JJJJJZZZZZ
JJJNNNNNNN
JqqNNNNNNN
JqqNNNNNNN
JJJJJJJJJe
qejjjjQQQQ
OOOOOOOQQQ
1 0
2 17 1
JJJJJJJJJJUUUBvsM
JJJJJJJJJJCCCggmx
1 3

"""





