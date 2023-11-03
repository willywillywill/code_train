word = """
A .- B -... C -.-. D -..
E . F ..-. G --. H ....
I .. J .--- K -.- L .-..
M -- N -. O --- P .--.
Q --.- R .-. S ... T -
U ..- V ...- W .-- X -..-
Y -.-- Z --..
""".split()
dit = {}
for i in range(0,len(word),2):
    dit[word[i+1]] = word[i]

for _ in range(int(input())):
    in1 = input().split()
    in1 = [ dit[i] for i in in1 ]
    print("".join(in1))

"""
5
... --- ...
-.-- --- ..-
.- -. -..
..
.... . .-.. .--.
"""