import random

class RandomPicker:
    def __init__(self,data):
        self.pool=data[:]

    def pick(self):
        if not self.pool:
            raise Exception("没有多余的元素！")
        index=random.randint(0,len(self.pool)-1)
        return self.pool.pop(index)

if __name__=="__main__":
    picker = RandomPicker([0,1,2,3])
    while True:
        try:
            print(picker.pick())
        except Exception as e:
            print(e)
            break