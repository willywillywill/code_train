
def del_s(str1):
    str1 = str1.replace(",","")
    str1 = str1.replace(";","")
    str1 = str1.replace("!","")
    str1 = str1.replace(".","")
    return str1

for _ in range(int(input())):
    s = list(map(del_s, input().split()))
    n = [ i for i in s if "s" in i.lower()]
    print(str(len(s))+","+str(len(n)))


"""
3
This is a sample file.
Hello WoUld!!
SOS! 
"""
