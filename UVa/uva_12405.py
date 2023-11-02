
for _ in range(int(input())):
    n = int(input())
    lst = list(input())
    num = 0
    for i in range(len(lst)):
        if lst[i] == ".":
            if i+2<n and lst[i+2]==".":
                lst[i] = "#"
                lst[i+1] = "#"
                lst[i+2] = "#"
                num+=1
            else:
                if i+1<n and lst[i+1]==".":
                    lst[i] = "#"
                    lst[i+1] = "#"
                    num += 1
                else:
                    lst[i] = "#"
                    num += 1
    print("Case %d:"%(_+1),num)

"""

15
5
.....
5
..#..
10
....##..#.
10
.....#....
9
....#....
12
....#....#..
10
..#..##...
13
..#..##....#.
4
####
3
.#.
4
##..
5
.....
6
.##...
4
..##
6
.#.#.#



"""