import requests,json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

s=requests.Session()
r=s.get('http://httpbin.org/stream/20')
if r.encoding is None: #encoding이 안되어있으면 None 반환
    r.encoding='utf-8'


for line in r.iter_lines(decode_unicode=True):
    b=json.loads(line)
    for e in b.keys():
        print("key: ",e,"values: ",b[e])
