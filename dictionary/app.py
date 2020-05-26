import json
import difflib  #비슷한 단어를 찾아주는 모듈

# 데이터 변수에 제이슨 파일을 딕셔너리 형태로 가져오기
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    simWord=difflib.get_close_matches(word,data.keys())
    if word in data :
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    else :
        for i in range(len(simWord)):
            print("혹시 입력한 단어가 %s 입니까?" %simWord[i])
            ans=input("맞으면 y 아니면 n 입력 : ")
            if ans=='y':
                return data[simWord[i]]
        return "그런 영단어는 없습니다. 철자를 체크하세요."

word=input("영어 단어 입력 : ")
output=translate(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)