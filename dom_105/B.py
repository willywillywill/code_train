dit = {
    "-----":0,
    ".----":1,
    "..---":2,
    "...--":3,
    "....-":4,
    ".....":5,
    "-....":6,
    "--...":7,
    "---..":8,
    "----.":9
}

for _ in range(int(input())):
    in1 = input().replace(" ","")
    for i in range(0,len(in1),5):
        print(dit[in1[i:i+5]], end="")
    print()

"""
3
.---- ..--- ...--
....- ..... -....
--... ---.. ----. 

2
.---- .---- -----
----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.
"""