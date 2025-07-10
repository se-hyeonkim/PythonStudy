'''아래와 같이 N 까지 합(Sigma) 을 구하는 공식을 함수 형태로 작성 후 출력하세요. 다양한 방법 사용

입력 : 10 
출력 결과 : 55'''

# 코딩 영역
# 사용자 입력
num = int(input("입력 : "))
sum_num = 0
for i in range(1, num + 1):
    sum_num += i
print(f"출력 결과 : {sum_num}")

# 수학 공식을 이용한 시그마 함수
def sigma_sum2(n):
    return n * (n + 1) // 2

print(f'ex2결과 : {sigma_sum2(10)}')

# 반복문을 이용한 시그마 함수
def sigma_sum1(n):
    tot = 0
    for i in range(1, n + 1):
        tot += i
    return tot

print(f'ex1결과 : {sigma_sum1(10)}')

# 내장 함수 sum()을 이용한 시그마 함수
def sigma_sum3(n):
    return sum(range(n + 1))

print(f'ex3결과 : {sigma_sum3(10)}')
