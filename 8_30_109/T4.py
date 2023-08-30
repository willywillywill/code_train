
n = 64

perim = lambda n: True if not len([ i for i in range(3,n) if n%i==0]) else False

arr = [ i for i in range(3,n) if perim(i) ]
num = [ set([arr[i],arr[j]]) for j in range(len(arr)) for i in range(len(arr)) if arr[i]+arr[j]==n]


"""
min_num = [ abs(i[0]-i[1]) for i in num ]
mn = min(min_num)
index_num = min_num.index(mn)
ab = num[index_num]
n = min_num[index_num]
"""