# 코딩 영역
filename = ["A", "B", "C", "D", "F", "G"]
contents = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
contents2 = [["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]]

import os

file_path = "../source/26-1/"

#방법 1
if os.path.exists(file_path):
    for i in range(len(filename)):
        new_file = os.path.join(file_path, filename[i] + ".txt")
        with open(new_file, 'w') as f:
            f.write(contents[i])
else:
    os.makedirs(file_path)
    for i in range(len(filename)):
            new_file = os.path.join(file_path, filename[i] + ".txt")
            with open(new_file, 'w') as f:
                f.write(contents[i])

#방법 2
def write_contents1(file_path):
    os.makedirs(file_path,exist_ok=True)

    for n, c in zip(filename, contents):
        with open(file_path + n + '.txt', 'w') as file:
            file.write(c)
#실행
write_contents1(file_path)


#방법 3(writelines 함수 사용. 리스트를 파일로 작성하기)
def write_contents2(file_path2):
    os.makedirs(file_path2,exist_ok=True)

    for n, c in zip(filename, contents2):
        with open(file_path2 + n + '.txt', 'w') as file:
            file.writelines(line + "\n" for line in c)
file_path2 = "../source/26-2/"

#실행
write_contents2(file_path2)
