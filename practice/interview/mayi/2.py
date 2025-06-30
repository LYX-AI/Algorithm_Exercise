'''
“有效括号匹配”问题，属于 LeetCode 第 20 题，常考。
我们来写一个完整的 Python 解法，并解释思路。

✅ 题目：
给定一个只包含 '()[]{}' 的字符串，判断是否括号成对出现且嵌套正确。
例如：

python
Copy
Edit
输入: s = "()[]{}"
输出: True

输入: s = "(]"
输出: False

输入: s = "([{}])"
输出: True
'''
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}  # 匹配规则

    for char in s:
        if char in mapping:  # 是右括号
            top = stack.pop() if stack else '#'  # 防止空栈
            if mapping[char] != top:
                return False
        else:
            stack.append(char)  # 左括号压栈

    return not stack  # 栈空表示匹配成功

# 示例测试
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([{}])"))    # True
