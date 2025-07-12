'''아래 3개의 리스트 를 {key : a , value : b * c} 형태의  Dict(딕셔너리) 구조 로 변경하세요. *다양한 방법 활용*

# 아래 조건 참조

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

출력 결과 : "{'one': 156.0, 'two': 148.0, 'three': 54.0, 'four': 315.0}"'''

# 코딩 영역

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

#방법1
result1 = {}

for x,y,z in zip(a,b,c):
    result1[x]=y*z

print('ex 1 결과 : ', result1)

#방법2
ex2 = {x: y *z for x, y, z in zip(a,b,c)}
print('ex 2 결과: ', ex2)
