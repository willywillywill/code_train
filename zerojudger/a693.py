from itertools import accumulate
while 1:
    try:
        n,m = list(map(int,input().split()))
        food = list(map(int,input().split()))
        food_sum = [0] + list(accumulate(food))

        for i in range(m):
            a,b = list(map(int,input().split()))
            print(food_sum[b]-food_sum[a-1])
    except:
        break
""" 
3 3
1 2 3
1 3
1 2
2 3
"""