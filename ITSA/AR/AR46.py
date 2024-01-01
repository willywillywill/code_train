lst = list(map(eval,input().split()))
lst = [ i**2.0 for i in lst ]
print("%.6f"%(sum(lst)))
