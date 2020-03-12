import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),"utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),"utf-8")

#matplotlib_converters : 날짜(시간)관련 #WARNING 제거
register_matplotlib_converters()

#조회 시작 날짜
start = datetime.datetime(2020,2,10)

#조회 마감 날짜
end = datetime.datetime(2020,3,10)

#네이버 주식 정보 조회
gs_naver = fdr.DataReader('035420',start,end)

#카카오 주식 정보 조회
gs_daum = fdr.DataReader('035720',start,end)

#중간 출력
# print(gs_naver)
# print(gs_daum)

#차트 윈도우 제목
fig = plt.figure("Chart Test")

#차트 사이즈 설정
fig.set_size_inches(10,6,forward=True)

#차트 설정1
plt.plot(gs_naver.index,gs_naver['Open'],'b',label="Naver")

#차트 설정2
plt.plot(gs_daum.index,gs_daum['Open'],'r',label="Daum")

#범례
plt.legend(loc='upper left')

#차트 제목
plt.title("naver & daum")

#x축 레이블
plt.xlabel("Date")

#y축 레이블
plt.ylabel("Open")
plt.show()
