dit = {"Tiger":0,"Lion":0}

for i in range(9):
    dit[input()] += 1

if dit["Tiger"] > dit["Lion"]:
    print("Tiger")
else:
    print("Lion")