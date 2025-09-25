1. Hello World 출력
print("Hello, World!")

2. 변수 저장 및 출력
name = "앨리스"
age = 20
print(name, "의 나이는", age, "세 입니다.")
3. 두 수 더하기
num1 = 5
num2 = 10
result = num1 + num2
print("덧셈 결과:", result)

4. 문자열 연결 (Concatenation)
str1 = "파이썬"
str2 = " 코딩"
combined = str1 + str2
print(combined)

5. 사용자 입력 받기
city = input("살고 싶은 도시 이름을 입력하세요: ")
print(city, "에 살고 싶으시군요!")

6. if/else 조건문
my_age = 15
if my_age >= 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

7. for 반복문
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print("좋아하는 과일:", fruit)

8. while 반복문
count = 1
while count <= 5:
    print(count)
    count += 1
    
9. 함수 정의 및 호출
def add_numbers(a, b):
    return a + b
sum_result = add_numbers(7, 3)
print("함수 호출 결과:", sum_result)

10. 리스트 (List) 사용
colors = ["빨강", "파랑", "노랑"]
colors.append("초록")  # 요소 추가
print("두 번째 색상:", colors[1])
print("전체 리스트:", colors)

11. 튜플 (Tuple) 사용
coordinates = (10, 20)
print("X 좌표:", coordinates[0])
# coordinates[0] = 5  # 오류 발생! 튜플은 변경 불가

12. 딕셔너리 (Dictionary) 사용
person = {"name": "철수", "age": 25, "job": "학생"}
print("철수의 나이:", person["age"])
person["age"] = 26 # 값 수정
print("수정된 나이:", person["age"])

13. 데이터 타입 변환
text_num = "10"
num_result = int(text_num) + 5
print("변환 후 덧셈 결과:", num_result)

14. 문자열 포매팅 (f-string)
item = "커피"
price = 4500
print(f"'{item}'의 가격은 {price}원 입니다.")

15. 간단한 모듈 사용
import math
print("파이 (π) 값:", math.pi)

16. 랜덤 숫자 생성
import random
random_num = random.randint(1, 100)
print("무작위 숫자:", random_num)

17. 리스트 정렬
scores = [85, 92, 78, 95]
scores.sort()
print("정렬된 점수:", scores)

18. 특정 문자열 포함 여부
sentence = "파이썬은 재미있습니다."
if "재미" in sentence:
    print("문장에 '재미'가 포함되어 있습니다.")
    
19. break 키워드
for i in range(10):
    if i == 5:
        print("5를 발견하여 반복 중단!")
        break
    print(i)
    
20. 짝수/홀수 판별
check_num = 14
if check_num % 2 == 0:
    print(f"{check_num}은 짝수입니다.")
else:
    print(f"{check_num}은 홀수입니다.")

##input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
단, while 문을 사용하세요.##

num = int(input("정수를 입력하세요"))

i = 0
while i < num:
    print('', num)
    i += 1


##정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.##

num = int(input())

i = 1

while i <= num:
    print(i, i * i)
    i = i + 1

##input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요. 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.##

num = int(input())

if num == 1:
    print('일')
elif num == 2:
    print('이')
elif num == 3:
    print('삼')

##사용자로부터 input()으로 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
단, 이번에는 for 문을 사용하세요##

num = int(input())

for i in range(num):
    print('', num)
