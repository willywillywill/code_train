# OK
dit = {
    "HELLO":"ENGLISH",
    "HOLA":"SPANISH",
    "HALLO":"GERMAN",
    "BONJOUR":"FRENCH",
    "CIAO":"ITALIAN",
    "ZDRAVSTVUJTE":"RUSSIAN",
    "n":"UNKNOWN"
}

n = 1
while 1:
    s = input()
    if s=="#":
        break

    if s in dit.keys():
        print("Case %d:"%(n), dit[s])
    else:
        print("Case %d:"%(n), dit["n"])
    
    n+=1