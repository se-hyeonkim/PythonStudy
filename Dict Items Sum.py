'''아래와 같은 Dict 구조에서 모든 value 값의 합(Sum) 을 구하세요. *가능한 모든 방법* 으로 코딩하세요.

d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

출력결과 : 2327'''

# 코딩 영역
d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}
total=0
for value in d.values():
    total += value

print(total)

total2=sum(d.values())
print(total2) 

print(sum([d[items] for items in d]))
