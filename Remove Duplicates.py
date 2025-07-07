'''아래와 리스트에서 중복 되는 원소 를 제거 후 출력하세요. 다양한 방법 코딩하세요.

x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]
출력 결과 : [1, 2, 3, 4, 5, 'a', 'b']'''

# 코딩 영역
x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]
ex1=list(set(x))
print(ex1)

#순서유지
from collections import OrderedDict
ex2=list(OrderedDict.fromkeys(x))
print(ex2)

#순서유지-전통
ex3=[]
for i in x:
    if i not in ex3:
        ex3.append(i)
print(ex3)

ex4=[]
result=[i for i in x if not (i in ex4 or ex4.append(i))]
print(result)


'''set() 함수란?
중복 제거: 리스트, 문자열, 튜플 등의 자료형에서 중복된 값을 제거하고 정렬되지 않은 집합을 만듭니다.

원소는 변경 불가능한(immutable) 타입이어야 합니다 (ex: 숫자, 문자열, 튜플 등은 가능, 리스트는 안 됨)

set()와 OrderedDict.fromkeys() 차이점

list(set(x))         
# 출력: ['banana', 'apple', 'kiwi'] (순서 보장 X)
list(OrderedDict.fromkeys(x))
# 출력: ['banana', 'apple', 'kiwi'] (처음 등장 순서 그대로)
'''


