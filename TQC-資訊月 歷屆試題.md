# TQC-資訊月

CLASS-1: TQC
CLASS-2: 解題

# TQC

## File

[108資訊月.pdf](TQC-pdf\108.pdf)

[109資訊月.pdf](TQC-pdf\109.pdf)

[110資訊月.pdf](TQC-pdf\110.pdf)

[111資訊月.pdf](TQC-pdf\111.pdf)

## TQC-108

- A1
    
    ```python
    x = int(input())
    y = int(input())
    z = int(input())
    
    h = ((x*60)+y)/60/60
    l = z/1.6/h
    print("Speed = %.1f"%(l))
    ```
    
- A2
    
    ```python
    n = int(input())
    k = 0
    for i in range(1,n+1):
        k+=((-1)**(i+1))/(2*i-1)
    print("%.4f"%(4*k))
    ```
    
- A3
    
    ```python
    in1 = int(input())
    in2 = int(input())
    
    lst = []
    for i in range(in1,in2+1):
        if (i%4==0 or i%6==0) and (i%12!=0):
            lst.append(i)
    
    k = 0
    for i in range(len(lst)):
        if i%10==0 and i:
            print()
            k=0
        print("%-4d"%(lst[i]),end="")
        k=1
    if k:
        print()
    print(len(lst))
    print(sum(lst))
    ```
    
- A4
    
    ```python
    num = 0
    ans = 0
    while 1:
        n = int(input())
        if  n==-9999:
            break
        num += n
        if num < 0:
            num=0
        ans = max(ans,num)
    print(ans)
    ```
    
- A5
    
    ```python
    n = int(input())
    
    def p(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    lst = [ i for i in range(2,n) if p(i) and str(i)==str(i)[::-1] ]
    
    k = 1
    l = 0
    j = 0
    for i in range(len(lst)):
        print("%-4d"%(lst[i]),end="")
        j=1
        l+=1
        if k==l:
            k+=1
            l=0
            j=0
            print()
    if j:
        print()
    print(sum(lst))
    ```
    

## TQC-109

- A1
    
    ```python
    lst = []
    for i in range(4):
        lst.append(eval(input()))
    print(*lst)
    print("Sun = %.2f"%(sum(lst)))
    print("Average = %.2f"%(sum(lst)/len(lst)))
    ```
    
- A2
    
    ```python
    n = int(input())
    
    if n >= 80:
        print("A")
    elif n >= 79:
        print("B")
    elif n >= 69:
        print("C")
    else:
        print("F")
    ```
    
- A3
    
    ```python
    n = int(input())
    def f(i):
        if i==2:
            return 1/((i-1)**0.5+i**0.5)
        return f(i-1)+(1/((i-1)**0.5+i**0.5))
    print("%.4f"%(f(n)))
    ```
    
- A4
    
    ```python
    n = int(input())
    
    def p(x):
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    
    lst = [str(n)]
    while n:
        l = 99999999
        for i in range(2,n):
            if p(i) and p(n-i):
                l = min(l,abs(i-(n-i)))
        n = l
        lst.append(str(l))
        if l==0 or l==2:
            break
    
    for i in lst:
        print(i,end=",")
    print()
    ```
    
- A5
    
    ```python
    s = list(input())
    
    stack = []
    arr = []
    out = []
    
    while s:
        ss = s.pop(0)
        if ss == "(":
            stack.append(ss)
            out.append("*")
            arr.append(len(out)-1)
        elif ss == ")":
            if stack:
                stack.pop(-1)
                out.append("*")
                arr.pop(-1)
            else:
                out.append("?")
        else:
            out.append("=")
    for i in arr:
        out[i] = "?"
    print("".join(out))
    ```
    

## TQC-110

- A1
    
    ```python
    x = int(input())
    y = int(input())
    
    r = ((x-5)**2+(y-6)**2)**0.5
    if r <= 15:
        print("Inside")
    else:
        print("Outside")
    ```
    
- A2
    
    ```python
    lst = [ i for i in range(int(input()),int(input())+1) if i%2==0 ]
    print(sum(lst))
    ```
    
- A3
    
    ```python
    n = int(input())
    lst = []
    
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    
    q1 = (n//4 if n%4==0 else n//4+1)-1
    q2 = (n//2 if n%2==0 else n//2+1)-1
    q3 = (n*3//4 if n*3%4==0 else n*3//4+1)-1
    print("%d,%d,%d"%(lst[q1],lst[q2],lst[q3]))
    ```
    
- A4
    
    ```python
    dit={}
    for i in input().lower():
        if i not in [" ","."]:
            dit[i] = dit.get(i,0)+1
    k = list(dit.items())
    k.sort(key=lambda x:(x[1],-ord(x[0])),reverse=True)
    
    print(sum([i[1] for i in k[:5] ]))
    print("".join([i[0] for i in k[:5] ]))
    ```
    
- A5
    
    ```python
    lst = list(map(str,input().split(',')))
    lst = [ [ int(j) for j in i] for i in lst]
    max_sum = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] in (1,2):
                for k in range(i,len(lst)):
                    for l in range(j, len(lst)):
                        n = [ lst[xx][yy] for xx in range(i,k+1) for yy in range(j,l+1) ]
                        if all([ m in (1,2)for m in n]):
                            sub_lst_sum = sum(n)
                            max_sum = max(max_sum, sub_lst_sum)             
    print(max_sum)
    ```
    

## TQC-111

- A1
    
    ```python
    lst = []
    for i in range(4):
        lst.append(float(input()))
    
    print("|%7.2f %7.2f|"%(lst[0],lst[1]))
    print("|%7.2f %7.2f|"%(lst[2],lst[3]))
    print("|%-7.2f %-7.2f|"%(lst[0],lst[1]))
    print("|%-7.2f %-7.2f|"%(lst[2],lst[3]))
    ```
    
- A2
    
    ```python
    lst = list(map(int,input().split()))
    lst.sort()
    
    if lst[-1] <= lst[0]+lst[1]:
        n = (lst[0]**2+lst[1]**2)**0.5
        if n == lst[-1]:
            print("Right triangle")
        elif n < lst[-1]:
            print("Obtuse triangle")
        else:
            print("Acute triangle")
    else:
        print("It can't be a triangle.")
    ```
    
- A3
    
    ```python
    lst = list(map(float,input().split()))
    c = lst[0]/lst[2]
    
    def f(i):
        if i==0:
            return 0
        return (lst[0]-(c*(i-1)))*((lst[1]/100)/12)+f(i-1)
    
    print(f(lst[2]))
    ```
    
- A4
    
    ```python
    k = int(input())
    
    def f(i):
        if i!=1:
            f(i-1)
        n = i*2
        print(" "*(k-i)+ "*"*((n-1)//2)+"*"+"*"*((n-1)//2))
    f(k)
    ```
    
- A5
    
    ```python
    in1 = list(map(int,input().split()))
    dp = [1 for i in range(len(in1))]
    
    for i in range(len(in1)):
        for j in range(i):
            if in1[i] > in1[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(dp)
    ```