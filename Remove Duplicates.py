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
