'''아래와 같이 Dictionary 에 {'c': 'banana', 'd': 'kiwi'} 를 추가하세요. *가능한 방법 모두 구현

d = {'a': 'apple', 'b': 'grape'}

출력 결과 : {'a': 'apple', 'b': 'grape', 'c': 'banana', 'd': 'kiwi'}'''

# 코딩 영역
d = {'a': 'apple', 'b': 'grape'}
d["c"]="banana"
d['d']='kiwi'
print(d)

e={'a': 'apple', 'b': 'grape'}
e.update({'c': 'banana', 'd': 'kiwi'})
print(e)
