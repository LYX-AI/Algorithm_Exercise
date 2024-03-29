def solution1(dicta,dictb):
    dictc={}
    for i in dacta.keys():
        for j in dictb.keys():
            if i==j:
                dicta[i]=dicta[i]+dictb[j]
    dictb.update(dicta)
    dictc.update(dictb)
    return dictc

    print(dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"},dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"})