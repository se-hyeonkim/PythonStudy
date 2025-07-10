'''아래 함수가 실행 시 에러가 발생하는 이유 를 생각해보세요. 함수 수정 후 정상적으로 실행해보세요. 결과값 : 1000

# 전역변수
x = 100

def test():
    x = x * 10
    return x

print(test())'''

# 코딩 영역
x=100

def test1():
    return x*10

print(f'ex1 결과 : {test1()}')

y=100

def test2():
    global y
    y*=10
    return y

print(f'{test2()}')
print(y)
