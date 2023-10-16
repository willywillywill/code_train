
out = [0,0,0]
n = 8765-1
if 0<=n<=2499:
    out[0] = 1
    out[1] = n//25+1
    out[2] = n%25+1
elif 2499 < n <= 7499:
    n -= 2500
    out[0] = 2
    out[1] = n//50+1
    out[2] = n%50+1
else:
    n -= 7500
    out[0] = 3
    out[1] = n//25+1
    out[2] = n%25+1
print(*out)