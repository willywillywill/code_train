lst = [float(input()) for i in range(4)]

print("|%7.2f %7.2f|"%(lst[0], lst[1]))
print("|%7.2f %7.2f|"%(lst[2], lst[3]))
print("|%-7.2f %-7.2f|"%(lst[0], lst[1]))
print("|%-7.2f %-7.2f|"%(lst[2], lst[3]))