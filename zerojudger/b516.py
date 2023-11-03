word_1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
word_2 = list("DEFGHIJKLMNOPQRSTUVWXYZABC")

for _ in range(int(input())):
    new_s = ""
    for i in input():
        new_s += word_2[word_1.index(i)]
    print(new_s)


"""
5
WIKIPEDIA
YOU
B
C
EF
"""