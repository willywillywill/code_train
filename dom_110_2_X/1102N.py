def distance(a:str, len_a:int, b:str, len_b:int):
    if len_a == 0:
        return len_b
    if len_b == 0:
        return len_a
    cos = 0
    if a[-1] == b[-1]:
        cos = 0
    else:
        cos = 1
    
    re1 = distance(a, len_a-1, b,  len_b) + 1
    re2 = distance(a, len_a  , b, len_b-1) + 1
    re3 = distance(a, len_a-1, b, len_b-1) + cos
    
    return min(re1,re2,re3)
        
a = "horse"
b = "ros"
print(distance(a,len(a),b,len(b)))    