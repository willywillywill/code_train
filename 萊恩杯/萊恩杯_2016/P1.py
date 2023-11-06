s = input()
s = [ ord(i) for i in s ]
print("%.3f"%(sum(s)/len(s)))