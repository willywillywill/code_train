
s = input()
if s != s[::-1]:
    print("no")
else:
    print("yes")

"""
s = input()
for i in range(len(s)//2):
    if s[i] != s[(i+1)*-1]:
        print("no")
        break
else:
    print("yes")
"""