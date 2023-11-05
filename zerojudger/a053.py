n = int(input())
if n <= 10:
    print(n*6)
elif n<=20:
    print(10*6+(n-10)*2)
elif n<40:
    print(10*6+10*2+(n-20)*1)
else:
    print(100)