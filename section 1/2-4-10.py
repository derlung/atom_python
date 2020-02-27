import os
import subprocess
import pytube


yt = pytube.YouTube("https://youtu.be/e2qG5uwDCW4")
vids = yt.streams.all()
for i in range(len(vids)):
    print(i,',',vids[i])

vum = int(input("다운 받을 화질을 입력하세요(0~22) :"))
new_filename = input("변환할 파일의 이름 :")


parent_dir = "D:/youtube01"
vids[vum].download(parent_dir)
default_filename=vids[0].default_filename
subprocess.call(['ffmpeg','-i',os.path.join(parent_dir,default_filename),
os.path.join("D:/youtube01/copyfiles",new_filename)])
print("동영상 다운로드 완료!")
