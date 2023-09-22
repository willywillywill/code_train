
def st(in1):
    for i in list(".,;!"):
        in1 = in1.replace(i, "")
    return in1

for _ in range(int(input())):
    in1 = list(map(str, st(input()).split()))
    print(len(in1))


"""
3
ThiV iV a Vample file.
Hello World!!
Hi!
"""