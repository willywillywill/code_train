in1 = int(input())
in2 = int(input())
sum = 0
for i in range(in1, in2+1):
    sum += i if i%2==0 else 0
print(sum)