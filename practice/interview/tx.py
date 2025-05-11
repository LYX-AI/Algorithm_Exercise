#随机字符串
import random
import string

def random_string(length=8,char=string.ascii_letters+string.digits+string.punctuation):
    return ''.join(random.choices(char,k=length))

if __name__=="__main__":
    print(random_string(12))