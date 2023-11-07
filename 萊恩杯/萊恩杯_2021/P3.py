k = int(input())
lst = [1]
while len(str(lst[-1])) <= k:
    lst.append((len(lst)+1)*lst[-1])
print(len(lst))