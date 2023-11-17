s = input()[::-1]
lst = []
out = []
for i in s:
    if i in lst:
        continue
    else:
        out.append(i)
        lst.append(i)
print("".join(out[::-1]))

"""
ABACDEAD
"""