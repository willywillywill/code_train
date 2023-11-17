txt = { chr(i):2 for i in range(ord("A"),ord("H")+1) }
txt.update({ chr(i):3 for i in range(ord("H")+1,ord("Z")+1)})

in1 = input()
for i in in1:
    txt[i] -= 1
out = []
for i in txt:
    if txt[i]:
        out.append(i)
if out:
    print("".join(out))
else:
    print("*")
"""
IJJSSTTJKKDEQQEHHIRRIFFGNNOOOAAUVVBBCCDGKLLLMMMNP
JJKMMNNNOOOPPPQUVVVWKKLXXIJQQRZZZAABBCRRSYYYCDDEEFFLLMWWXGGHHIISSTTTUU
"""