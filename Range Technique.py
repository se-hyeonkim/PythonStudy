''' 다음과 같이 30 ~ -10 까지 -2씩 감소한 결과를 리스트로 출력하세요.
출력 결과 : [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]'''

# 코딩 영역
a=30
ex1=[]

for i in range(30,-12,-2):
    ex1.append(i)

print(ex1)

ex2=list(range(30,-12,-2))
print(ex2)

ex3=list(filter(lambda x: x >= -10, range(30, -11, -2)))
print(ex3)
