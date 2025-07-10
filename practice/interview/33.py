'''
字符串adcababc 求最大不重复字符串长度？
'''
def finde_maxlength(s:str)->int:
    max_length=0
    temp=set()
    left=0
    for right in range(len(s)):
        while s[right] in temp:
            temp.remove(s[left])
            left+=1
        temp.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length
if __name__=='__main__':
    s='adcabcabc'
    print(finde_maxlength(s))