           


n = 0
m = 1
num = []
perim = lambda n: True if not len([ i for i in range(2,int(n**0.5)+1) if n%i==0]) else False

for i in range(2,int(input())):
    if perim(i):
        k = list(str(i))
        if k == k[::-1]:
            num.append(i)
            print("%-4d"%(i),end="")
            n+=1

            if n==m:
                print()
                m+=1
                n=0
if n!=0:
    print()
print(sum(num))
