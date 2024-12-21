'''
题目1
编写一个程序，接受用户输入的字符串，并打印出该字符串的长度和首字母。

这个题目可以帮你复习字符串的基本操作，如获取长度和索引访问

'''
user_input=input("please enter the number")

print("the length of the number is",len(user_input))
if len(user_input)>0:
    print('字符串的首字母是', user_input[0])
else:
    print('is empty')
'''
创建一个列表包含数字1到10，使用切片取出其中的第2到第5项。
'''
numbers=list(range(1,11))

selected_number=numbers[1:5]
print("选中的数字",selected_number)

'''
使用for循环遍历上述列表，并打印每个元素的平方值。

这将帮你复习for循环和算术运算。下面是实现这个需求的代码
'''

for number in numbers:
    print(f"{number}的平方是{number**2}")