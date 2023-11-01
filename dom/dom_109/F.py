# ! ! ! https://zh.wikipedia.org/zh-tw/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

for _ in range(int(input())):
    lst = list(map(int,input().split()))
    print(max_subarray(lst))

"""
6
1 2
10 -1 -1 2
216 2
-2 1 -3 4 -1 2 1 -5 10
-2 -3 4 -1 -2 1 5 -3
-2 3 4 1 2 1 5 -3
"""