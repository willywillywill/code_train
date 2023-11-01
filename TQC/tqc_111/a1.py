lst = []
for i in range(4):
    lst.append(float(input()))

print("|%7.2f %7.2f|"%(lst[0],lst[1]))
print("|%7.2f %7.2f|"%(lst[2],lst[3]))
print("|%-7.2f %-7.2f|"%(lst[0],lst[1]))
print("|%-7.2f %-7.2f|"%(lst[2],lst[3]))

"""
23.12
395.3
100.4617
564.329
"""