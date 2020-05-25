import random

first=1
last=100
number=random.randint(first,last)

name=input('당신의 이름은?\n')
print('안녕하세요 '+name+'님 , '+ str(first)+'에서 '+str(last)+'까지 숫자중 하나를 생각합니다.')

count=0
while count<6:
    guess=int(input('맞춰보세요\n'))
    if count==5:
        print('틀렸네요. 정답은 '+str(number)+'입니다.')
    elif guess>number:
        print('그 숫자보다 작은수')
    elif guess<number:
        print('그 숫자보다 큰수')
    else :
        print('잘 맞췄어요 '+name+'님 '+str(count+1)+'만에 맞췄어요 !')
        break
    count+=1
