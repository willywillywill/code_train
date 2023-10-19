import heapq

lst = [[0,1,4],[0,2,3],[0,3,2],[0,4,1]]
heapq.heapify(lst)
print(lst)
lst = heapq.nsmallest(len(lst),lst,key=lambda x:x[2])
print(lst)
a = heapq.heappop(lst)
print(a)