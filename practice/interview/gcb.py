def gcb(a:int,b:int):
    while b != 0 :
        a , b = b , a%b
    return abs(a)
