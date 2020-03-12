import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(500,1000,size=(100,4)),columns=[2015,2016,2017,2018])
print(df)

#csv index , header (True False 이용)
#excel index(None) header (True,false)

df.to_excel("D:/atom_python/6-3.xlsx",index=None,header=True)
