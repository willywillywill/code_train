

data = []
for i in range(int(input())):
    data.append(list(map(int,input().split())))

data.sort(key= lambda x:x[0])

points = [data.pop(0)]
for tmp in data:
    if tmp[0] > points[-1][1]:
        points.append(tmp)
    elif tmp[1] > points[-1][1]:
        points[-1][1] = tmp[1]
length = 0
for point in points:
    length += point[1]-point[0]
print(length)

"""
5
160 180
150 200
280 300
300 330
190 210
"""