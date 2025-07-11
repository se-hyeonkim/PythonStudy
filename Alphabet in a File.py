'''/source 폴더에 23-1.txt 파일이름으로 대문자 알파벳(A-Z)을 공백 으로 구분 후 파일로 쓰세요. *아래 조건을 참고하세요*

# 아래 조건 참조

파일명 & 경로 = "../source/23-1.txt"
파일 출력 결과 : "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"'''

# 코딩 영역
#방법1
filepath="../source/23-1.txt"

alphabet_list = [chr(i) for i in range(65, 91)]  # A(65) ~ Z(90)

# 2. 파일에 쓰기
with open(filepath, "w") as file:
    for letter in alphabet_list:
        file.write(letter + " ")

#방법2
def write_alphabet1(file_path):
    with open(file_path, 'w') as file:
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #str은 시퀀스형
            file.write(letter+" ")

print(f'ex1결과 : {write_alphabet1(filepath)}')

with open(filepath, "r") as f:
    content = f.read()
    print(f"ex1 결과 : {content}")


#방법3
import string

def write_alphabet2(file_path):
    with open(file_path, 'w') as file:
        for letter in string.ascii_uppercase:
            file.write(letter+" ")

write_alphabet2(filepath)

with open(filepath, "r") as f:
    contents = f.read()
    print(f"ex2 결과 : {contents}")

print(f'ex2결과 : {write_alphabet2("../source/23-2.txt")}') #파일을 쓰기만 해서 none이 나옴.
