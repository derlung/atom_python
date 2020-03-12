import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

df2=pd.read_csv('D:/atom_python/csv_s2.csv',sep=';',skiprows=[0],names=["First name","Test1","Test2","Test3","Final","Grade"])
print(df2)
df2["Sum"] = df2[["Test1","Test2","Test3","Final"]].sum(axis=1)
df2["Avg"] = df2[["Test1","Test2","Test3","Final"]].mean(axis=1)
print(df2)

#csv쓰기
df2.to_csv('D:/atom_python/result1.csv',index=False)
