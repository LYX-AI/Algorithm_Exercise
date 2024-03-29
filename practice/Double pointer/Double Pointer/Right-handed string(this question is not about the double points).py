'''
Topic:
The right-handed string is to put the words at the tail of the string to the head of the string
for example there is the number n=2 and there is the string ""abcdefg"" 
then will get the ""fgabcde"


example:
样例输入：

2
abcdefg 
样例输出：

fgabcde
'''




class solution:
    def Right_handed_string(self,strng,n):
        List=list(strng)
        point=len(List)-1
        for i in range(n):
            temp=List.pop()
            List.insert(0,temp)
        return "".join(List)

a=solution()
print(a.Right_handed_string(strng="abcdefg",n=2))

