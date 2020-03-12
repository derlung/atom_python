import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

df1=pd.read_excel('D:/atom_python/excel_s1.xlsx',header=0)
print(df1)
df1['State']=df1['State'].str.replace(' ',' | ')
print(df1)

df1['Avg'] = df1[['2018','2019','2020']].mean(axis=1).round(2)
df1['Sum'] = df1[['2018','2019','2020']].sum(axis=1)
print(df1)

print(df1[['2018','2019','2020']].max(axis=0))
print(df1[['2018','2019','2020']].min(axis=0))

print(df1.describe())

#excel 쓰기
df1.to_excel('D:/atom_python/result_s1.xlsx',index=None)
