# 1. 계산에 사용되는 핵심 함수 정의  
def add(x, y):
    """덧셈을 수행합니다."""
    return x + y

def subtract(x, y):
    """뺄셈을 수행합니다."""
    return x - y

def multiply(x, y):
    """곱셈을 수행합니다."""
    return x * y

def divide(x, y):
    """나눗셈을 수행합니다."""
    # 0으로 나누는 경우를 대비해 None을 반환
    if y == 0:
        return None 
    return x / y

# 2. 메인 계산기 함수
def calculator():
    print("=== 간단한 텍스트 계산기 ===")
    print("지원 연산: +, -, *, /")
    print("종료하려면 'quit'를 입력하세요.")
    
    # 딕셔너리를 사용하여 연산 기호와 함수를 연결
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    while True:
        try:
            # 첫 번째 숫자 입력
            num1_input = input("\n첫 번째 숫자를 입력하세요 (종료: quit): ")
            if num1_input.lower() == 'quit':
                break
            
            num1 = float(num1_input) # 숫자가 아닐 경우 ValueError 발생 가능
            
            # 연산 기호 입력
            operator = input("연산자 (+, -, *, /)를 입력하세요: ")
            if operator not in operations:
                print("오류: 유효하지 않은 연산자입니다.")
                continue

            # 두 번째 숫자 입력
            num2 = float(input("두 번째 숫자를 입력하세요: "))

            # 3. 함수를 이용한 계산 실행
            calculation_function = operations[operator]
            result = calculation_function(num1, num2)

            # 4. 결과 출력 및 특수 예외 처리
            if operator == '/' and result is None:
                print("오류: 숫자를 0으로 나눌 수 없습니다.")
            else:
                print(f"결과: {num1} {operator} {num2} = {result}")

        except ValueError:
            # 숫자가 아닌 문자열을 입력했을 때 처리
            print("오류: 유효한 숫자를 입력해 주세요.")
        except Exception as e:
            # 기타 예상치 못한 오류 처리
            print(f"알 수 없는 오류가 발생했습니다: {e}")

    print("=== 계산기를 종료합니다 ===")

# 프로그램 시작
if __name__ == "__main__":
    calculator()
