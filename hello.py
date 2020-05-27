
# import 시 모듈을 사용 가능
print('hello 모듈 시작')
print('hello.py __name__:',__name__)    #__name__변수 출력 
                                        # import 시 모듈 이름
                                        # hello.py 실행시 __main__
print('hello 모듈 끝')

if __name__=='__main__':
    print('hello.py를 실행할 때만 보입니다.')