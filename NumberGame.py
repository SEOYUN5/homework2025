import random

# 1. 게임 설정
MAX_ATTEMPTS = 5
SECRET_NUMBER = random.randint(1, 100)
attempts = 0

print("=== 숫자 맞추기 게임을 시작합니다! ===")
print(f"저는 1부터 100 사이의 비밀 숫자를 생각했습니다. 기회는 총 {MAX_ATTEMPTS}번입니다.")

# 2. 게임 루프 시작
while attempts < MAX_ATTEMPTS:
    attempts += 1
    
    # 사용자에게 숫자 입력 받기 및 예외 처리
    try:
        guess = int(input(f"\n[{attempts}/{MAX_ATTEMPTS}번째 시도] 숫자를 입력하세요: "))
    except ValueError:
        print("경고: 유효한 숫자를 입력해 주세요.")
        # 유효하지 않은 입력은 시도 횟수에 포함하지 않기 위해 횟수를 되돌림
        attempts -= 1 
        continue # 다음 반복으로 넘어감

    # 3. 입력된 숫자 비교 및 피드백
    if guess == SECRET_NUMBER:
        print(f"\n🎉 **정답입니다!** {attempts}번 만에 맞히셨습니다. 축하해요!")
        break # 정답을 맞혔으므로 루프 종료
    elif guess < SECRET_NUMBER:
        print("👆 'Up'! 제가 생각한 숫자보다 더 높습니다.")
    else: # guess > SECRET_NUMBER
        print("👇 'Down'! 제가 생각한 숫자보다 더 낮습니다.")

# 4. 게임 종료 처리
if guess != SECRET_NUMBER:
    print("\n😢 **아쉽습니다.** 기회를 모두 사용했습니다.")
    print(f"제가 생각한 비밀 숫자는 **{SECRET_NUMBER}**였습니다.")

print("\n=== 게임 종료 ===")
