in1 = input().lower()

a1 = in1[0].upper()+in1[1:]
a2 = in1.upper()
a3 = ""
m = 1
for i in in1:
    if m:
        a3 += i.upper()
        m = 0
    else:
        a3 += i
    if not i.isalpha():
        m = 1
    
print(a1)
print(a2)
print(a3)
print(in1)