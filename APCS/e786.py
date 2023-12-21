
s = input()
if len(s)%2==0:
    if s[:len(s)//2] == s[len(s)//2:][::-1]:
        print("YES")
        print(s[:len(s)//2])
    else:
        print("NO")
else:
    print("NO")

"""
MERRYXMAS SAMXYRREM
MERRYXMASSAMXYRREM
"""