def f(s):
    s.sort(key=lambda x:int(x))
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            return False
    return True

n = int(input())
m = int("9"*n)
for i in range(m,-1,-1):
    i = str(i)
    for j in range(len(i)):
        if int(i[:j+1])%(j+1) != 0:
            break
    else:
        if f(list(str(i))):
            print(i)
            break