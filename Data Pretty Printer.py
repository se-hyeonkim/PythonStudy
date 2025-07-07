'''
아래와 같이 코드를 작성 후 실행하세요. json 형식을 구조에 맞게(예쁘게) 출력하세요.(pprint)
from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

response_json = response.read()

d = json.loads(response_json)

# 출력 결과 비교(print)
print(d)

# 출력 결과 비교(pprint)
from pprint import pprint

pprint(d)'''

# 코딩 영역

from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

response_json = response.read()

d = json.loads(response_json)
print(d)

print()
print()
print()

# 출력 결과 비교(print)
from pprint import pprint

pprint(d)

print()
print()
print()

pprint(d, depth=3, indent=2, width=200)
