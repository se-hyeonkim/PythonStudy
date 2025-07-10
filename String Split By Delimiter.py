'''아래와 같은 문장을 공백 으로 구분 후 단어 개수를 출력하는 함수 를 작성 후 실행하세요. input 함수 가능

in_str = "Suppose we have few words that are separated by spaces."

출력 결과 : 10'''

# 코딩 영역
in_str = "Suppose we have few words that are separated by spaces."
word=list(in_str.split(sep=' '))
word_count=len(word)
print(f'출력 결과 : {word_count}')
