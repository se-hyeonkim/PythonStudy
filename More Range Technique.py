'''아래와 같이 1부터 20 까지 홀수 * 10, 짝수는 그대로 리스트로 출력하세요.

출력 결과 : [10, 2, 30, 4, 50, 6, 70, 8, 90, 10, 110, 12, 130, 14, 150, 16, 170, 18, 190, 20]'''

# 코딩 영역
ex1=[]
a=1
#방법1
for i in range(a,21,1):
    if i%2==1:
        ex1.append(10*i)
    else:
        ex1.append(i)

print(ex1)

#방법2
ex2=[x*10 if x%2==1 else x for x in range(1,21)]
print(ex2)
