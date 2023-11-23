roma_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
                 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

for _ in range(int(input())):
    n = int(input())
    ans = ""
    while n:
        for i in roma_dict:
            if n >= i:
                k = n//i
                ans += roma_dict[i]*k
                n -= k*i
    print(ans)