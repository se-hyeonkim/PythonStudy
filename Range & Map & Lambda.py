'''아래와 같이 1부터 15 까지 원소 * 10 결과는 문자열 리스트로 출력하세요. range, map, lambda 사용

출력 결과 : ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150"]'''

# 코딩 영역
ex1=list(map(lambda i: str(i*10),range(1,16)))
print(ex1)

ex2=[]
for i in range(1,16):
    ex2.append(str(i*10))
print(ex2)

print([str(y*10) for y in range(1,16)])
