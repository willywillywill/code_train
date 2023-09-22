

for _ in range(int(input())):
    in1 = input().split("/")
    in2 = list(map(int,in1[1].split(".")))
    in1 = list(map(int,in1[0].split(".")))
    k = [ str(in1[i] & in2[i]) for i in range(len(in1)) ]
    print(".".join(k))