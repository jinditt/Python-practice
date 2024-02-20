text = 'Python is a programming language'
temp = ''
for i in text.split():
 print(i)
 if i == 'language':
        temp = i.upper() + ' ' + temp
 else:
    temp = i +' '+ temp
print(temp)

temp= ''
s='I like cooking'
for i in range(len(s)):
    ch= '#' if i =  else s[i]
    temp+=ch
print(temp)

nlist=[]
num=input('숫자 입력:')
for i in num:
    nlist.append(i)
for j in nlist:
    print(int(j)*'♥')

date='2021-11-12'
print(date)
print(type(date))

from datetime import datetime, timedelta
date=datetime.strptime(date,'%Y-%m-%d')
print(date)
print(type(date))

from datetime import datetime, timedelta, date
date2=input('날짜 입력(연/월/일):')
date2=datetime.strptime(date2,'%Y/%m/%d')
print(type(date2))
print(f'10년 뒤:{date2.year+10}년 {date2.month}월 {date2.day}일')
