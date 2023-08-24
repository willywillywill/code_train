def sum(x):
    if x==1:
        return 1
    else:
        return sum(x-1)+x
    
print(sum(5))