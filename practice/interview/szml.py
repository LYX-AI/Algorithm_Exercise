'''
回文字符串（Palindrome） 是指正读和反读都相同的字符串。即字符串与其反转后的字符串完全一致。例如：

单词语："madam"、"racecar"、"level"

中文："上海自来水来自海上"

数字："12321"

忽略空格/符号："A man, a plan, a canal: Panama"（处理后为 "amanaplanacanalpanama"）
'''

def is_palindrome(s:str)->bool:
    fins=''
    for c in s:
        if c.isalnum():
           fins+= c.lower()
    left ,right=0 , len(fins)-1
    while left<right:
            if fins[left]!=fins[right]:
                return False
            left+=1
            right-=1
    return True