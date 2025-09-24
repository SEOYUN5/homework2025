import random
import string


def generate_password():
    """사용자 설정에 따라 무작위 비밀번호를 생성하는 함수"""
    print("=== 강력한 비밀번호 생성기 ===")
    
    # 1. 비밀번호 길이 입력 받기
    while True:
        try:
            length = int(input("비밀번호의 길이를 입력하세요 (예: 12): "))
            if length > 0:
                break
            else:
                print("길이는 1보다 커야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")
            
    # 2. 포함할 문자 종류 선택
    print("\n비밀번호에 포함할 문자 종류를 선택하세요 (Y/N로 입력):")
    
    use_lowercase = input("  소문자 (a-z)를 포함할까요? (Y/N): ").upper() == 'Y'
    use_uppercase = input("  대문자 (A-Z)를 포함할까요? (Y/N): ").upper() == 'Y'
    use_digits = input("  숫자 (0-9)를 포함할까요? (Y/N): ").upper() == 'Y'
    use_symbols = input("  특수 문자 (!@#$ 등)를 포함할까요? (Y/N): ").upper() == 'Y'

    # 포함할 전체 문자 집합 구성
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # 유효성 검사: 최소한 하나의 문자 종류는 선택했는지 확인
    if not characters:
        print("\n⚠️ 오류: 비밀번호를 생성하려면 최소한 하나의 문자 종류를 선택해야 합니다. ⚠️")
        return # 함수 종료
    
    # 3. 비밀번호 생성
    password = ""
    for _ in range(length):
        # characters 문자 집합에서 무작위로 문자 하나를 선택하여 추가
        password += random.choice(characters)
        
    print(f"\n✅ 생성된 비밀번호: {password}")
    print(f"✅ 비밀번호 길이: {len(password)}")

# 함수 실행
if __name__ == "__main__":
    generate_password()
