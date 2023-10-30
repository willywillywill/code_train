def p(y):
    for i in range(2,y):
        if y%i==0:
            return False
    return True

n = int(input())
y = n^2 + n + 41
print( "質數" if p(y) else "非質數" )