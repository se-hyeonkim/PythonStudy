'''아래 함수가 실행 시 에러가 발생하는 이유 를 생각해보세요. 함수 수정 후 정상적으로 실행해보세요.


# 함수 선언
def greet(msg="Good morning!", name):
    return "Hi! " + name + ', ' + msg

# 실행
print(greet("Kim"))
print(greet("Park", "How do you do?"))'''

# 코딩 영역

#모든 인자가 디폴트 값일 경우
#모든 인자가 디폴트 값x 경우
#디폴트 값 인자가 뒤로

# 함수 선언
def greet(name, msg="Good morning!"):
    return "Hi! " + name + ', ' + msg

# 실행
print(greet("Kim")) 
print(greet("Park", "How do you do?"))

#예제2
def add1(a, b=10, c=15):
    print(a,b, c)
    return a+b+c

print(f'{add1(15)}')
print(f'{add1(b=100,c=25,a=30)}')

#예제3
def add2(*d):
    tot = 0
    for i in d:
        tot += i
    return tot

print(f'{add2(10,30)}')
print(f'{add2(*(i for i in range(1,11)))}')
print(*(i for i in range(1,11)))
