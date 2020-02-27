import requests,json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


payload = {'key1':'name1','key2':'name2'}
r=requests.put('http://jsonplaceholder.typicode.com/posts/1')
print(r.text)
