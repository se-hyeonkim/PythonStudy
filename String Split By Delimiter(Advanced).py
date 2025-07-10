'''/source 폴더의 22-2.txt 파일을 공백 구분 후 단어 개수를 출력하는 함수 를 작성 후 실행하세요. *콤마의 경우 두 단어로 취급*

# Hi! Kim,Eun 의 경우 -> 3개

in_str = "../source/22-1.txt"

출력 결과 : 72'''

# 코딩 영역
in_str= """The adjective "deep" in deep learning refers to the use of multiple layers in the network. 
Early work showed that a linear perceptron cannot be a universal classifier,but 
that a network with a nonpolynomial activation function with one hidden layer of unbounded width can. 
Deep learning is a modern variation which is concerned with an unbounded number of layers of bounded size,which
permits practical application and optimized implementation,while retaining theoretical"""
#1
def cnt_word1(filepath):
    with open(filepath, 'r') as file:
        text=file.read()
    text=text.replace(',',' ')


    #print(text)

    text_list=text.split()
    #print(text_list)
    return len(text_list)

#print(f'{cnt_word1("../source/22-1.txt")}')

#2
import re

def cnt_word2(filepath):
    with open(filepath,'r') as file:
        txt=file.read()

    txt_list=re.split(" |,",txt)
    txt_list = [w for w in txt_list if w]  # 빈 문자열 제거(리스트 컴프리헨션)
    #print(txt_list)
    return len(txt_list)
print(f'{cnt_word2("../source/22-1.txt")}')
