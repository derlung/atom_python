import pandas as pd
import xlrd
import openpyxl

# #기본 읽기
# df=pd.read_excel('D:/atom_python/excel_s1.xlsx',sheet_name=0)
# # print(df)
# # print(df.head(10))
# # print(df.tail())
#
#
# #행,footer 스킵
# df=pd.read_excel('D:/atom_python/excel_s1.xlsx',skiprows=[0],skipfooter=45)
# print(df)

#헤더 정의
# df=pd.read_excel('D:/atom_python/excel_s1.xlsx',skiprows=[0],header=None,names=["state",2018,2019,2020])
# print(df)

#특정값 치환
# df=pd.read_excel('D:/atom_python/excel_s1.xlsx',header=0,na_values='...',converters={"2018":lambda w:w if w>60000 else None})

#인덱스 재정의
df=pd.read_excel('D:/atom_python/excel_s1.xlsx')
print(df.rename(index=lambda x:x+1))
print(list(df.rename(index=lambda x:x+1).index))
