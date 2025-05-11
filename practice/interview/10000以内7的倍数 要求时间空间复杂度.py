def generate_encrypted():
    result=[]
    for num in range(7,10000,7):
        result.append(str(num))
    return '-'.join(result)