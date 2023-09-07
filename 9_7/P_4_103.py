# !! set
for _ in range(int(input())):
    set_1 = set(list(map(int, input().split()))[1:])
    set_2 = set(list(map(int, input().split()))[1:])
    print(len(set_1 & set_2))


