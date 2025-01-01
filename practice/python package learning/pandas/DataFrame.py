import pandas as pd
data=[['Google',10],['Runoob',12],['Wiki',13]]
df=pd.DataFrame(data,columns=['Site','Age'])
df['Site']=df['Site'].astype(str)
df['Age']=df['Age'].astype(float)
print(df)

data={'Site':['Google','Runoob','Wiki'],'Age':[10,12,13]}
df=pd.DataFrame(data)
print('------------------------')
print(df.loc[0])
print(df.loc[1])
print('------------------------')
print(df)
print(f'返回第一行和第二行\n{df.loc[[0,1]]}')
print('--------常用的基本方法-----------')
data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df2=pd.DataFrame(data)
print(df2)
print(f'查看前两行的数据\n{df2.head(2)}')
print('》》》》》》》》》》》》》》》》》》')
print(df2.info)
print(f'获取统计信息{df2.describe()}')
print('按照年龄排序')
df_sorted=df2.sort_values(by='Age',ascending=False)
print(df_sorted)
print('选择指定的列')
print(df2[['Name','Age']])
print('按城市分组计算年龄')
print(df2.groupby('City')['Age'].mean())
