from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


#Dict 선언
r_data = {'City':['서울','대구','부산','대전'],'Total1':[55000,47000,49000,46000],'Total2':[65000,57000,53000,48000]}
i_data = {'one','two','three','four'}

#출력
# print(type(r_data))
# print(r_data)

#DataFrame 정의
df = DataFrame(r_data,index=i_data)
df2 = DataFrame(r_data,index=i_data,columns=['Total1','Total2','City'])
# print(df2)
#
#
# print(df2.index)
# print(df2.values)
#
# print(df2.describe())

#값 순회
for data in df.values:
    print(data)
    # for i in range(data.size):
    #     print("{} {}".format(i,data[i]))
    for i,e in enumerate(data):
        print(i,e)
