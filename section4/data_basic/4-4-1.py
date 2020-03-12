import simplejson as json


#Dict (json0) 선언
data={} #Dict
data['people']=[] #array
data['people'].append({'name':'kim','website':'naver.com','from':'Seoul'})
data['people'].append({'name':'park','website':'naver.com','from':'Seoul'})
data['people'].append({'name':'jin','website':'naver.com','from':'Seoul'})
data['people'].append({'name':'chang','website':'naver.com','from':'Seoul'})
print(data)

#Dict -> Str(json)
e=json.dumps(data)
print(type(e))
print(e)

#Str -> Dict(json)
d = json.loads(e)
print(type(d))
print(d)

with open('D:/atom_python/member.json','w') as f:
    f.write(e)

with open('D:/atom_python/member.json','r') as infile:
    r=json.loads(infile.read()) #dump 로 읽어들일때는 loads -> load 로 사용하교 read메소드도 사용안한다. 객체만
    print("==========")
    print(type(r))
    print(r)

    for p in r['people']:
        print("name : " + p["name"])
        print('website : '+p['website'])
        print('From : '+p['from'])
        print('')
        t=p['grade']
        grade =''
        for g in t:
            grade = grade + ' ' + str(g)
        print("grade:",grade.lstrip())
        print('')
