import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")

imgUrl = "https://seoul-p-studio.bunjang.net/product/95185749_1_1546874483_w640.jpg"
htmlUrl="https://www.google.com/"

savePath1="D:/gms/Atom/test1.jpg"
savePath2 = "D:/gms/Atom/index.html"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlUrl,savePath2)
print("다운로드완료")
