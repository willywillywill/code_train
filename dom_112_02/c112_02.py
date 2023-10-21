s = input()
num = 0
for i in range(len(s)):
    for j in range(i):
        if s[i-j:i+j+1] == s[i-j:i+j+1][::-1]:
            num = max(num,len(s[i-j:i+j+1]))
        
print(num)
"""
123batabba321
"""