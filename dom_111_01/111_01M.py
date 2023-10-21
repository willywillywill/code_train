
in1 = input()[2:-2].split("],[")
in1 = [ list(map(int,i.split(","))) for i in in1 ]
in1 = in1[::-1]

arr = [ [ 0 for j in range(len(in1[0]))] for i in range(len(in1)) ]

for i in range(len(in1)):
    for j in range(len(in1[0])):
        arr[i][j] = in1[j][i]
print("[",end="")
for i in range(len(arr)):
    print("[",end="")
    for j in range(len(arr[i])):
        print(arr[i][j],end= "" if j==len(arr[i])-1 else "," )
    print("]",end= "" if i==len(arr[i])-1 else ",")
print("]")

"""
[[1,2,3],[4,5,6],[7,8,9]]
[[20,19,18,17],[16,15,14,13],[12,11,10,9],[8,7,6,5]]
"""