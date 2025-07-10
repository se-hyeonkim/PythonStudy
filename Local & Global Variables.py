'''아래 함수 실행 후 Step1, Step2 -> a, b, x, y 결과를 예측 해보세요.

def test(x, y):
    global a
    a = 49
    x,y = y,x
    b = 53
    b = 7
    a = 135
    # 예상1
    print('Step1 : ', a, b, x, y)

a, b, x, y = 8, 13, 33,44 

# 함수 실행
test(23, 7)

# 예상2
print('Step2 : ', a, b, x, y)'''

# 코딩 영역

def test(x,y):
    global a
    a=49
    x,y=y,x
    b=53
    b=7
    a=135
    #예상1
    print(f'ex1 결과 : {a,b,x,y}')

a,b,x,y = 8,13,33,44

test(23,7)

print(f'ex2 결과 : {a,b,x,y}')

'''ex1 결과 : (135, 7, 7, 23)
ex2 결과 : (135, 13, 33, 44)'''
