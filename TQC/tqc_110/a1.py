x = int(input())
y = int(input())

r = ((x-5)**2+(y-6)**2)**0.5
if r <= 15:
    print("Inside")
else:
    print("Outside")