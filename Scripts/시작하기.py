print('안녕하세요') #프린트 함수 => 화면출력
print('이름이 무엇인가요?') #이름묻기
myName = input() #입력받기
print('만나서 반갑습니다. ' + myName)
print('당신의 이름의 길이는: ')
print(len(myName)) # len 문자열의 길이
print('당신의 나이는?')
myAge = input() # 나이 입력
print('당신은 내년에 ' + str(int(myAge) +1) + '살 입니다.')