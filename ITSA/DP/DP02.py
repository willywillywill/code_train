

n,m = map(int,input().split())
w_lst = list(map(int,input().split()))
m_lst = list(map(int,input().split()))
m_we = m_lst[2]

def find(k,values):
    memo = [-1]*(k+1)
    memo[0] = 0
    for item in range(1,k+1):
        memo[item] = k+1
    
    for item in range(1,k+1):
        for coin in values:
            if item-coin < 0:
                continue
            memo[item] = min(
                memo[item],
                memo[item-coin]+1
            )
    return memo

memo = find(m_we, w_lst)
print(memo)
print(memo[m_we])

"""
2 5
3 5
1 5 2 7 8
3 5
2 5 2
20 1 2 4 9
"""