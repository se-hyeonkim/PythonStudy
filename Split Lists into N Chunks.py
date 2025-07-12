'''아래와 같이 주어진 리스트 를 N개 단위로 출력 결과 와 같이 리스트 로 생성 & 출력 하세요. *함수 가능*

# 기본 리스트
x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# N -> 3
출력 결과 : [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R'],['S','T','U'],['V','W','X'],['Y','Z']]
    
# N -> 5
출력 결과 : [['A','B','C','D','E'],['F','G','H','I','J'],['K','L','M','N','O'],['P','Q','R','S','T'],['U','V','W','X','Y'],['Z']]'''

# 코딩 영역
# 기본 리스트
x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#방법 1
# N -> 3
ex1 = []
chunk_size = 3
for i in range(0, len(x), chunk_size) :
    ex1.append(x[i:i+chunk_size])
print(ex1)

# N -> 5
ex1_2 = []
chunk_size = 5
for i in range(0, len(x), chunk_size) :
    ex1_2.append(x[i:i+chunk_size])
print(ex1_2)

#방법 2
# N -> 3
ex2 = [x[i:i+3] for i in range(0, len(x), 3)]
print(ex2)
# N -> 5
ex2 = [x[i:i+5] for i in range(0, len(x), 5)]
print(ex2)

#방법3
def split_n_list(split_size=3):
    split_list=list()

    for i in range(0, len(x), split_size):
        split_list.append(x[i:i+3])

    return split_list

print('ex 3 결과 : ', split_n_list())
