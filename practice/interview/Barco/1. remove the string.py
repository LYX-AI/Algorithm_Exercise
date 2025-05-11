'''
题目1：删除字符串中的重复字符
题目描述： 给定一个字符串 s，删除其中重复出现的字符，只保留第一次出现的字符，返回去重后的结果串
geeksforgeeks.org
。输出中字符的顺序须与原串中第一次出现的顺序一致。例如：
arduino
Copy
Edit
输入: s = "geeksforgeeks"
输出: "geksfor"

'''
def remove_duplicates(s:str)->str:
    see=set()
    result=[]
    for char in s:
        if char not in see:
            see.add(char)
            result.append(char)
    return  ''.join(result)

if __name__=='__main__':
    s='geeksforgeeks'
    print(remove_duplicates(s))
