'''아래와 같은 딕셔너리 구조에서 Value 값이 25 이상 필터링 후 출력하세요. 다양한 방법 으로 코딩하세요.

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}
출력 결과 : {'b': 33, 'd': 26, 'f': 120}'''

# 코딩 영역

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}
ex1={}
for k,v in d.items():
    if v>=25:
        ex1[k]=v
print(ex1)

ex2={k: v for k, v in d.items() if v >=25}
print(ex2)

print(dict((k, v) for k, v in d.items() if v >=25))

ex3=dict(filter(lambda x: x[1]>=25, d.items()))
print(ex3)
