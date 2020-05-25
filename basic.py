'''
x = 10
print(x)

예제 2
x = 1
y = 2
z = 3
print(x)
print(y)
print(z)
예제 3
x = 1
y = 1.1
z = '1'
print(type(x))
print(type(y))
print(type(z))

크다 작다 예제
x = -10
if x*2 > x:
    print('크다')
else:
    print('작거나 같다.')

if 문
name = '셀리스'
if name == '앨리스':
    print('반가워요' + name)
print('종료')

if elif else 문
name = '밥'
if name == '앨리스':
    print('당신이 앨리스군요')
elif name == '밥':
    print('당신이 밥이군요')    
else:
    print('누구신가요?')

예제
name = input('이름 입력 ? : ')
if name != '':
    print('당신의 이름은 ' + name + '입니다.')
else:
    print('이름을 입력하지 않았군요!')

while 반복문
count = 0
while count < 3:
    print('횟수:', count)
    count += 1   # count = count + 1

name = ''
while name != '홍길동':
    print('이름을 입력하세요.')
    name = input()
print('종료')

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print('나무를 %d번 찍습니다.'%treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다!.')

continue : 다시 조건으로 돌아감
break: 반복문 끝내기
count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    if count == 8:
        break

for 문
animals = ['땅다람쥐', '바다코끼리', '스컹크', '아나콘다', '코알라', '하이에나', '바다소']
for a in animals:
    print(a)

for ch in 'abcdefg':
    print(ch)

for i in (1,2,3,4,5):
    print(i)

for n in range(10): # 0 ~ n-1
    print(n)

구구단 전체 출력
for i in range(2,10):        # ①번 for문
     for j in range(1, 10):   # ②번 for문
         print('{}X{}={}'.format( i, j, i*j), end=" ") 
     print('') 

''' 
"""
 여러열 주석
"""

'''
연습문제

#1 
a = 'Life is too short, you need python'

if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
'''

#예제 2
# n = 1
# sum = 0
# while n <= 1000:
#     if n % 3 == 0:
#         sum = sum + n
#     n = n + 1

# sum = 0
# for i in range(1,1001):
#     if i % 3 == 0:
#         sum = sum + i  

# print(sum)

#예제 3
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1

# print()

# for i in range(1,6):
#     print('*' * i)

#예제 4
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# 합계 = 0
# for a in A:
#     합계 = 합계 + a
# 평균점수 = 합계/len(A)
# print('평균 점수는 {} 입니다.'.format(평균점수))

#컴프리헨션
# 홀수 = []
# for n in range(1,11):
#     if n % 2 == 1:
#         홀수.append(n)
# print(홀수)

# 홀수 = [n for n in range(1,101) if n%2 == 1]

# print(홀수)

# 외부 모듈 
# import sys
# print('헬로우')
# sys.exit() # 프로그램 종료
# print('월드!!!') # 이 문장은 실행이 안됨

# 내부 함수
# def is_all_upper(text: str) -> bool:
#     for ch in list(text):
#         if ch.isupper():
#             pass
#         else:
#             return False
#     return True

# if __name__ == '__main__':
#     print("Example:")
#     print(is_all_upper('ALL UPPER'))


#     print("Coding complete? Click 'Check' to earn cool rewards!")


# 내부 함수
# 함수
# def hello():
#     print('하이!')
#     print('안녕!')
#     print('니 하오!')

# hello()
# hello()
# hello()

# 매개변수가 있는 함수
# def hello(name):
#     print('하이 ' + name)

# hello('길동')
# hello('펭수')

# def add10(num):
#     return num+10

# print(add10(1))
# print(add10(2))

# 예제1
# def is_odd(num):
#     if num%2==0:
#         print('짝수')
#     else :
#         print('홀수')

# is_odd(1)
# is_odd(2)

# 예제2
# def foo(*arg):
#     return sum(arg)/len(arg)

# print(foo(10,20,30))


# 전역 변수
# x=10
# def foo():
#     print(x)

# foo()
# print(x)

# 지역 변수
# def spam():
#     eggs=99
#     bacon()
#     print(eggs)

# def bacon():
#     ham=101
#     eggs=0

# spam()

# 에러처리 try/except
# def div10(num):
#     try:
#         return 10/num
#     except ZeroDivisionError: #무슨 에러인지 모를 경우 에러 명을 안적어도 된다.
#         print('에러: 0으로 나눌 수 없음')
#         # 리턴이 없는 함수는 none을 리턴

# print(div10(2))
# print(div10(0))
# print(div10(5))

# 예제 1
# myList=[1,0.2,'가']   
# print(myList)

# 예제 2
# myList=[1,0.2,'가',[2,0.3,'나']]
# print(myList)
# print(myList[-1])

# 딕셔너리 {키값:값}
# 키값으로 검색, 순서가 없다(인덱스 없음)
# myd={1:'a','b':2}
# print(myd[1])
# print(myd[2]) #키값에 2가없기 때문에 KeyError 발생

# myCat={'사이즈':'소형','색':'연한갈색','특기':'잠자기'}
# # print(list(myCat.keys()))
# # print(list(myCat.values()))
# # print(list(myCat.items()))

# # for문으로 key, value 값을 전체 출력

# # for k in myCat.values():
# #     print(k)

# # get() 함수 : 해당 값을 리턴, 없을때 (기본 = None)

# print(myCat.get('color','없음')) # 해당 키 값이 없을때 뒤의 값으로 대체됨
# print(myCat.get('색','없음'))

# count={}
# for ch in 'hello':
#     count.setdefault(ch,0) # 딕셔너리에 키에 ch의 값을 주고 해당 키의값을 모두 0으로 만듦
#     count[ch]=count[ch]+1 #hello에서 l은 두개이므로 키'l'이 두번 실행되므로 2가 들어간다.

# print(count)

import pprint

msg='''
“25일 낮 기준 이태원 클럽 관련 확진자 총 237명”

김동우 기자 love@kmib.co.kr

▶ 네이버에서 국민일보를 구독하세요(클릭)
▶ 국민일보 홈페이지 바로가기

GoodNews paper ⓒ 국민일보(www.kmib.co.kr), 무단전재 및 재배포금지'''
count={}
for ch in msg:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1

pprint.pprint(count)