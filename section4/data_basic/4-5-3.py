import pandas as pd
import numpy as np
#
# df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=list('ABCD'))
# print(df)
df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=["ONE","TWO","THREE","FOUR"])
# #랜덤으로 DataFrame ,굘훈 마루기
# df=pd.DataFrame(np.random.randn(100,4),columns=list('ABCD'))
# print(df)

#CSV쓰가
df.to_csv('D:/atom_python/result2.csv',index=False,header=False)
print('commit')
