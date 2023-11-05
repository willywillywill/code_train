dit = {
    "00":"A", 
    "01":"B",
    "100":"0",
    "101":"1",
    "1100":"2",
    "1101":"3",
    "11100":"4",
    "11101":"5",
    "111100":"6",
    "111101":"7",
    "111110":"8",
    "111111":"9"
}
while 1:
    try:
        for _ in range(int(input())):
            in1 = list(input())
            save = ""
            out = ""
            while in1:
                save += in1.pop(0)
                if save in dit:
                    out += dit[save]
                    save = ""
            if "A" in out and "B" in out:
                print("%s,%sA%sB"%("".join(out[0:out.index("A")-1]), "".join(out[out.index("A")-1]), "".join(out[out.index("B")-1])  ))
            elif "A" in out:
                print("%s,%sA"%("".join(out[0:out.index("A")-1]), "".join(out[out.index("A")-1])  ))
            elif "B" in out:
                print("%s,%sB"%("".join(out[0:out.index("B")-1]), "".join(out[out.index("B")-1])  ))
    except:
        break