import pandas as pd
series=pd.Series([1,2,3,4],name='A')

print(series)

#自定义索引
custom_index=[1,2,3,4]
series_with_index=pd.Series([1,2,3,4],index=custom_index,name='A')
print(series_with_index)

data=[1,2,3,4,5,6]
index=['a','b','c','d','e','f']
s=pd.Series(data,index=index)

print(f'前两行的数据是\n{s.head(2)}')

s_doubled=s.map(lambda x:x*2)
print(f'加倍元素是{s_doubled}')

s_sum=s.cumsum()
print('累计求和：\n',s_sum)

#检查缺失的值
print('缺失值判断：', s.isnull())

#排序
sorted_s=s.sort_values()
print('排序后的Series:',sorted_s)

print(s[1:4])