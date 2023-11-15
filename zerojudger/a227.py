def hanoi(n, road_from, road_temp, road_to):
    if n==1:
        print("Move ring {} from {} to {}".format(n,road_from, road_to))
        return
    
    hanoi(n-1, road_from, road_to, road_temp)
    print("Move ring {} from {} to {}".format(n,road_from, road_to))
    hanoi(n-1, road_temp, road_from, road_to)

while 1:
    try:
        hanoi(int(input()),"A","B","C")
        print()
    except:
        break