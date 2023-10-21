"""
a,b,c,d,e
e,b,c,d,a
把a移除掉->扣掉區間內a大於區間數字的數量
把e移除掉->扣掉區間內區間數字大於e的數量
把e放到新位置->加上區間內數字小於e的數量
把a放到新位置->加上區間內a大於數字的數量

結論：
對於每次修改，會進行交換的地方為[l,r]
newans = 
+ans
-區間內比arr[l]小的數量
-區間內比arr[r]大的數量
+區間內比arr[r]小的數量
+區間內比arr[l]大的數量

因此對於兩個數字交換，子任務就是分別找出上面這四個數字
在求上面四個數字時，可以發現他們性質相同，所以可以用相同的函式解決
因為是很多區間的問題，每個區間不可能都要用O(n)解決，所以要用分塊演算法
然後會查詢每一塊比arr[l]小的數量，所以可以先對每一塊進行排序，這樣就可以在O(log n)內查找出數量
對於左塊跟右塊則直接進行暴力判斷，複雜度為根號n

對於每個完整區塊都要用二分搜，把複雜度從O(n**0.5)變成O(log n**0.5)

1.區間內比arr[l]小的數量
先找出左不完整塊中所有比arr[l]小的數量
對於每個中間塊透過bisect找出所有比arr[l]小的數字數量
再找出右不完整塊中所有比arr[l]小的數量
結果相加就是答案

2.區間內比arr[l]大的數量
先找出左不完整塊中所有比arr[l]大的數量
對於每個中間塊透過bisect找出所有比arr[l]大的數字數量
再找出右不完整塊中所有比arr[l]大的數量
結果相加就是答案

3.區間內比arr[r]小的數量
先找出左不完整塊中所有比arr[r]小的數量
對於每個中間塊透過bisect找出所有比arr[r]小的數字數量
再找出右不完整塊中所有比arr[r]小的數量
結果相加就是答案

4.區間內比arr[r]大的數量
先找出左不完整塊中所有比arr[r]大的數量
對於每個中間塊透過bisect找出所有比arr[r]大的數字數量
再找出右不完整塊中所有比arr[r]大的數量
結果相加就是答案

對於左不完整塊的暴力搜索，複雜度為O(sqrt(n))
對於中間最多為sqrt(n)塊搜索，每一塊搜索為O(log sqrt(n))，因此複雜度為O(sqrt(n)*log sqrt(n))
對於右不完整塊的暴力搜索，複雜度為O(sqrt(n))

故每次搜尋的總複雜度為O(sqrt(n)*log sqrt(n))

對於最開始每一區塊間的排序複雜度為O(n log n)
對於所有詢問總複雜度為O(q(sqrt(n)*log sqrt(n)))
總體時間複雜度為O(max(n log n,q*(sqrt(n)*log sqrt(n)))) 安全通過
"""

from bisect import *
#紀錄每個數字在哪個方塊的哪個位置
blockindex = {}

#創建方塊陣列同時記錄各數字在方塊中的位置
def create_block(arr):
    n = len(arr)
    k = int(n**0.5)
    block = [[] for i in range(n//k+1*(n%k!=0))]
    for i in range(0,len(arr)):
        block[i//k].append(arr[i])
        blockindex[arr[i]] = [i//k,i%k]
    return block

#取得在arr某個l到r的區間中所有比val大或是比val小的數字
def getnum(arr,block,val,l,r,s):
    n = len(arr)
    k = int(n**0.5)
    startblock = l//k
    endblock = r//k
    total = 0
    for i in range(startblock,endblock+1):
        #計算目前本區塊區段範圍
        x = k*i
        y = min(n,k*i+k-1)

        #完全區塊->二分搜直接找出數字數量
        if(x>=l and y<=r):
            if(s=="small"):
                total+=bisect_left(block[i],val)
            else:
                total+=len(block[i])-bisect_right(block[i],val)
        #左區塊->暴力搜
        elif(x<l):
            for j in range(l,min(r,y)+1):
                if(s=="small"):
                    if(val>arr[j]):
                        total+=1
                else:
                    if(val<arr[j]):
                        total+=1
        #右區塊->暴力搜
        else:
            for j in range(x,r+1):
                if(s=="small"):
                    if(val>arr[j]):
                        total+=1
                else:
                    if(val<arr[j]):
                        total+=1
    return total

#交換數字，arr和block都要進行交換
def change(arr,block,a,b):
    a_num = arr[a]
    b_num = arr[b]
    
    #arr內容交換
    arr[a],arr[b] = arr[b],arr[a]

    #塊中數字交換與座標紀錄交換
    a_blockindex = blockindex[a_num]
    b_blockindex = blockindex[b_num]

    #塊中內容進行交換
    block[a_blockindex[0]][a_blockindex[1]],block[b_blockindex[0]][b_blockindex[1]] = block[b_blockindex[0]][b_blockindex[1]],block[a_blockindex[0]][a_blockindex[1]]
    ablock = a_blockindex[0]
    bblock = b_blockindex[0]
    
    #重新排序
    block[ablock].sort()
    #排序後更新該塊每個數字的位置
    for i in range(0,len(block[ablock])):
        blockindex[block[ablock][i]] = [ablock,i]
    
    #重新排序
    block[bblock].sort()
    #排序後更新該塊每個數字的位置
    for i in range(0,len(block[bblock])):
        blockindex[block[bblock][i]] = [bblock,i]


n,q = map(int,input().split())
arr = [i for i in range(1,n+1)]
#建立塊陣列
block = create_block(arr)
ans = 0
for i in range(q):
    a,b = map(int,input().split())
    a-=1
    b-=1
    if(a>b):
        a,b = b,a
    if(a==b):
        print(ans)
        continue
    #對於交換後的ans變動進行處理
    ans-=getnum(arr,block,arr[a],a+1,b,"small")
    ans+=getnum(arr,block,arr[a],a+1,b,"big")
    ans-=getnum(arr,block,arr[b],a,b-1,"big")
    ans+=getnum(arr,block,arr[b],a,b-1,"small")
    #特殊處理
    if(arr[a]>arr[b]):
        ans+=1
    else:
        ans-=1

    #交換數字並輸出答案
    change(arr,block,a,b)
    print(ans)