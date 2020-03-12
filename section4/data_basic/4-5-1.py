import pandas as pd
import csv
#
#
# df = pd.read_csv('D:/atom_python/csv_s1.csv',skiprows=[0],header=None)
# print(df)
#
# df = pd.read_csv('D:/atom_python/csv_s2.csv',skiprows=[0],header=None)
# print(df)
#
# df = pd.read_csv('D:/atom_python/csv_s2.csv',skiprows=[0],header=None,names=["에취","감기는","싫어","콜록"])
# print(df)
#
# df = pd.read_csv('D:/atom_python/csv_s2.csv',skiprows=[0],header=None,names=["에취","감기는","싫어","콜록"],index_col=[0])
# print(df)
#
# df = pd.read_csv('D:/atom_python/csv_s2.csv',skiprows=[0],header=None,na_values=["JAN"])
# print(df)
#
# print(pd.isnull(df))
#
#

# df = pd.read_csv('D:/atom_python/csv_s2.csv',skiprows=[0],header=None,names=["Nonth",2018,2019,2020])
# print(df)
# print(df.index)
# print(df.index.values)
# print(df.index.values.tolist())

# print(df.rename(index=lambda x:x*10).index)
df2=pd.read_csv('D:/atom_python/csv_s2.csv',sep=';',skiprows=[0],names=["First name","Test1","Test2","Test3","Final","Grade"])
print(df2)
print(df2['Grade'])
df2['Grade']=df2['Grade'].str.replace('C','A++')
print(df2)

#평균 컬럼 추가
df2['AVG']=df2[['Test1','Test2','Test3','Final']].mean(axis=1)
print(df2)
#합계 컬럼 추가
df2['SUM'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)
