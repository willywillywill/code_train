from sys import stdin
def flip(matrix):
    return list(reversed(matrix))
def rotate(matrix):
    tmp=[]
    row=len(matrix)
    col=len(matrix[0])
    for i in range(col):
        combine=[]
        for j in range(row):
            combine.append(matrix[j][i])
        tmp.append(combine)
    return list(reversed(tmp))
for read in stdin:
    R,C,M=map(int,read.rstrip().split())
    matrix=[]
    for i in range(R): matrix.append([int(x) for x in input().split()])
    operates=[int(x) for x in input().split()]
    for i in list(reversed(operates)):
        if i==0: matrix=rotate(matrix)
        elif i==1: matrix=flip(matrix)
    print(len(matrix),len(matrix[0]))
    for i in matrix: print(*i,sep=' ')
"""

def a(arr):
    c_arr = [ [ j for j in i ] for i in arr ]
    for i in range(len(arr)):
        arr[i] = c_arr[len(arr)-i-1]
    return arr
def b(arr):
    tmp = []
    for i in range(len(arr[0])):
        l = []
        for j in range(len(arr)):
            l.append(arr[j][i])
        tmp.append(l)
    return list(reversed(tmp)).copy()


while 1:
    try:
        r,c,m = map(int,input().split())
        arr = []
        for i in range(r):
            arr.append(list(map(int,input().split())))
        for i in list(reversed(list(map(int,input().split())))): # ! reversed
            if i:
                arr = a(arr)
            else:
                arr = b(arr)

        print(len(arr),len(arr[0]))
        for i in arr:
            print(*i)
    except:
        break


"""