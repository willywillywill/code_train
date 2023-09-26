
def del_s(str1):
    str1.replace(",","")
    str1.replace(";","")
    str1.replace("!","")
    str1.replace(".","")
    return str1

for _ in range(int(input())):
    s = list(map(str, input().split()))

    n = 0
    for i in s:
        i = del_s(i)
        if "S" in i or "s" in i:
            n+=1
    print(n)



"""
3
This is a sample file.
Hello WoUld!!
SOS! 
"""
