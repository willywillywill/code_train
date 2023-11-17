lst = list(input())
l = [ int(i) for i in lst ]
s = sum(l)
p = 10 - s%10 if s%10 else 0
lst.append(str(p))
print("".join(lst))
