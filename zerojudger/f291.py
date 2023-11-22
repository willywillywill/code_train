s = input()
a = int("".join([ i for i in s if i.isdigit() ]))
b = "".join([ i for i in s if i.isalpha() ][::-1])

i = 0
n = 0
for x in b:
    n += (ord(x)-64) * 26**i
    i += 1
print(n*a)