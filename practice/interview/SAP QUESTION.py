'''
Topic:
**题目：**
一个电工在Timberland市的8个街道灯上做了一些错误的电路连接。这些错误导致，如果一盏街灯相邻的灯在前一夜都是开着（表示为1）或都是关着（表示为0），那么这盏灯在当晚会关闭（变为0）。除此之外，这盏灯会照常点亮（变为1）。在街道的两端各有一个街道灯，只有一个相邻的街道灯，因此可以假设这两个灯在任何时候都是关闭的（0）。街道灯状态的变化是基于前一天的状态，而不是同一天。

由于这个故障，市民在晚上驾车时遇到困难，他们已经向联邦公路管理局投诉。基于这些投诉，负责人要求在M天后提交一份街道灯状态的报告。

输入数据将包括：
- 第一行输入是两个整数，分别代表矩阵的行数（N）和列数（M）。
- 接下来的N行数据，每行包含M个用空格隔开的整数，代表矩阵的元素。

输出数据应该包括：
- 在M天后，街道灯状态的整数列表。

约束条件是：
- 1 ≤ 天数 ≤ 10^6

示例输入：
```
8
1 1 1 0 1 1 1 1
2
```

示例输出：
```
0 0 0 0 1 1 0
```

这是一个简化版的题目描述，原题中可能包含更多细节或具有不同的格式要求。在实际编程任务中，应该根据完整的题目要求来实现代码。

原题目描述：
Mr. Woods, an electrician for Timberland city, has made some faulty connections on eight street lights. 
The errors cause a street light to go OFF if the street lights adjacent to that light were both ON (represented as 1) 
or both OFF (represented as 0) on the previous night. 
Otherwise, the light will go ON as normal. 
The two street lights at the end of the road have only a single adjacent street light, 
so the light at the end can be assumed to be always OFF. 
The state of the lights on a particular day is considered for the following day, 
not for the same day.Because of this fault, people are having difficulty driving on the road at night. 
They have filed a complaint to the Head of the Federal Highway Administration. 
Based on this complaint the head has ordered a report of the state of street lights after M days.

Input
The first line of input consists of an integer- current State_size, representing the number of street lights (N).
The next line consists of N space-separated integers- current State, representing the current state of the street lights (i.e., either 0 or 1).
The last line consists of an integer - days, representing the number of days (M).

Output
Print eight space-separated integers representing the state of the street lights after M days.

Constraints
1 ≤ days ≤ 10^6

Example
Input:
8
1 1 1 0 1 1 1 1
2

Output:
0 0 0 0 1 1 0

Explanation:
The street light at position 0 has as neighboring street lights 0 (assumption) and 1. So, on the next day, it will be 1.
The street light at position 1 has as its neighboring street lights both 1. So, on the next day, it will be 0.
The street light at position 2 has as one of its neighboring street lights 0 and the other one 1. So, the next day, it will be 1.
The street light at position 3 is 0 and both its neighboring street lights are 1. So, the next day, the street light at position 3 will be 0 only.
Similarly, we can find the state of the remaining street lights for the next day.
So, the state of the street lights after the first day is 1 0 1 0 1 0 0 1.
After two days, the state of the street lights is 0 0 0 0 1 1 0.
'''
def streetLight(currentState, days):
    #currentState是当前的路灯状态
    #头部和尾部的路灯信息被置为0
    currentState=[0]+currentState+[0]
    for _ in range(days):
        newState=currentState[:]
        for i in range[1,len(currentState-1)]:
            if currentState[i-1]==currentState[i+1]:
                newState[i]=0
            else:
                newState[i]=1
    return currentState[1:-1]

def main():
    current_state_size=int(input())
    currentState=list(map(int, input().split()))
    '''
    要学习的知识点：
    split：
        .split() 方法在没有指定分隔符的情况下，默认使用空白字符进行分割，这包括空格、制表符（\t）、换行符（\n）和回车符（\r）。这意味着它会识别这些空白字符并在遇到它们时将字符串分割成多个部分。

例如：

text = "hello world\npython programming\tis fun"
parts = text.split()
在这个例子中，parts 将是一个包含以下字符串的列表：['hello', 'world', 'python', 'programming', 'is', 'fun']。注意，原字符串中的换行符和制表符都被视为分隔符，与空格一样处理。

map：
    map 函数的基本语法如下：

map(function, iterable, ...)
function：这是一个函数，map 将这个函数应用于iterable的每个元素。
iterable：一个或多个可迭代对象，其元素将被function函数处理。
    '''
    days=int(input())
    result=streetLight(currentState,days)
    print(" ".join(str(res) for res in result))

