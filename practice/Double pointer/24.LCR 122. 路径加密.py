'''
describe of the issue
    Suppose a path is denoted as the string path, with "." as the separator. You need to encrypt the path by replacing the separator in path with a space "", and return the encrypted string.

    example:
        示例 1：

输入：path = "a.aef.qerf.bb"

输出："a aef qerf bb"


'''
class Solution:
    def pathEncryption(self, path: str):
        lst=list(path)
        for i in range(len(lst)):
            if lst[i]=='.':
                lst[i]=" "
        return ''.join(lst)

'''
There is another topic is same like this, but is more complex then this 

The topic is :
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."
#
思路
train of thought:
    first step:  Resize the array to its padded size
    seconde step:traverse the array from the tail of the array to the head of the array
        This way defined two pointers, left and right ; 
        the right is point to the tail of the array which has already be expended
        the left is point to the tail of the array which has not been expended
there are two advantages of using this way
1.Don't need to apply the new array
2."Populate elements from the back to avoid the issue of shifting all elements after each addition when populating from the front
'''
class Solution:
    def replaceSpace(s: str):
        # Resize the array to its padded size
        count=s.count(" ")
        res=list(s)
        res.extend([' ']*2*count)
        # traverse the array from the tail of the head of the head of the array
        right,left=len(res)-1,len(s)-1
        while left>=0:
            if res[left] !=' ':
                res[right]=res[left]
                right-=1
            else:
                res[right-2:right+1]="%20"
                right-=3
            left-=1
        return ''.join(res)

# Solution2 Create a new array to new list to store the result
    def replaceSpace2(s: str):
        res=[]
        for i in range(len(s)) :
            if s[i]==" ":
                res.append('20%')
            else:
                res.append(s[i])
        return ''.join(res)


print(Solution.replaceSpace2("We are happy"))


        