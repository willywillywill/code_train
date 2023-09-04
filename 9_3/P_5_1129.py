s = input().split()
ss = s[2:-2]
ss = s[:2]+[ "*"*len(i) for i in ss ]+s[-2:]
print(" ".join(ss))
