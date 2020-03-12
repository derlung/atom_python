import datetime
import FinanceDataReader as fdr
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

#조회 시작 날짜
start = datetime.datetime(2020,2,19)
#조회 마감 날짜
end = datetime.datetime(2020,3,4)

#한국거래소 상장종목 전체
# df_krx = fdr.StockListing('KRX')

#리스트 10개 출력
# print(df_krx.head(10))

#출력
# print(df_krx['Symbol'])
# print(df_krx.iloc[0])

#미국 애플사 금융정보
# df_app=fdr.DataReader('AAPL',start,end)
# print(df_app.head(10))
# print(df_app.loc['2018-02-23'])

#미국 아마존 금융정보
df_app=fdr.DataReader('AMZN',start,end)
print(df_app.head(10))
print(df_app.loc['2020-02-24'])

#미국 구글 금융정보
df_app=fdr.DataReader('GOOGL',start,end)
print(df_app.head(10))
print(df_app.loc['2020-02-24'])
