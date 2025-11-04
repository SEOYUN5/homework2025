# https://www.acmicpc.net/workbook/view/459 여기를 참고하여 작성하였습니다.

from collections import Counter

# 주사위 세계 
def dice_world_outcomes(n_dice):
    """N개의 주사위를 굴릴 때 나오는 총 경우의 수(6^N)를 반환합니다."""
    return 6 ** n_dice

# 크냐? 
def compare_numbers(a, b):
    """두 수 A와 B를 비교합니다."""
    if a > b:
        return "A > B"
    elif a < b:
        return "A < B"
    else:
        return "A == B"

# 주사위 게임 
def calculate_dice_game_score(a, b, c):
    """3개 주사위 눈(a, b, c)에 따라 상금을 계산합니다."""
    if a == b and b == c:
        return 10000 + a * 1000
    elif a == b or b == c or a == c:
        same_eye = a if a == b or a == c else b
        return 1000 + same_eye * 100
    else:
        return max(a, b, c) * 100

# 개표 
def get_winner(votes):
    """투표 목록에서 가장 많은 표를 얻은 항목을 반환합니다."""
    vote_counts = Counter(votes)
    if not vote_counts:
        return "투표 결과 없음"
    
    most_common = vote_counts.most_common(2)
    winner = most_common[0][0]
    max_votes = most_common[0][1]
    
    if len(most_common) > 1 and most_common[1][1] == max_votes:
        return "동점입니다"
    
    return f"승자: {winner} ({max_votes}표)"

# 배우와 약수 
def find_divisors(n):
    """양의 정수 n의 모든 약수를 찾아 리스트로 반환합니다."""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors)

# OX퀴즈 
def calculate_ox_quiz_score(results):
    """O/X 퀴즈 결과를 바탕으로 점수를 계산합니다. O는 가산점."""
    score = 0
    consecutive_o = 0
    for result in results:
        if result == 'O':
            consecutive_o += 1
            score += consecutive_o
        else:
            consecutive_o = 0
    return score

# 약수들의 합 
def sum_of_divisors(n):
    """정수 n의 모든 약수들의 합을 반환합니다. (자기 자신 포함)"""
    return sum(find_divisors(n))

# 큰 수 A+B (10757)
def big_number_addition(a_str, b_str):
    """큰 수 문자열 A와 B를 더한 결과를 문자열로 반환합니다."""
    a = int(a_str)
    b = int(b_str)
    return str(a + b)


# 알람 시계 
def set_alarm_early(h, m):
    """H시 M분보다 45분 일찍인 시간을 계산합니다."""
    m -= 45
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h = 23
    return f"{h}시 {m}분"

# 펠린드롬인지 확인하기 
def is_palindrome(word):
    """문자열이 회문인지 판별합니다. (True/False 반환)"""
    return word.lower() == word[::-1].lower()

# 사분면 
def check_quadrant(x, y):
    """좌표 (x, y)가 속하는 사분면 번호를 반환합니다."""
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    return "축 또는 원점"

# 전자레인지 
def min_microwave_ops(t):
    """T초를 맞추기 위한 5분, 1분, 10초 버튼의 최소 횟수를 계산합니다."""
    if t % 10 != 0:
        return "불가능"
    
    a, t = divmod(t, 300) # 5분 = 300초
    b, t = divmod(t, 60)  # 1분 = 60초
    c, t = divmod(t, 10) # 10초
    
    return f"A:{a}, B:{b}, C:{c}"

# 과자 
def calculate_money_needed(k, n, m):
    """과자 K원짜리 N개 구매 시 부족한 금액 M을 반환합니다."""
    total_cost = k * n
    needed = total_cost - m
    return max(0, needed)

# 네 번째 째 
def find_fourth_point(points):
    """직사각형 세 점의 좌표를 받아 네 번째 점을 계산합니다."""
    # points = [[x1, y1], [x2, y2], [x3, y3]]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    # XOR 연산을 사용하여 겹치는 좌표를 상쇄하고 홀로 남은 좌표를 찾음
    x4 = xs[0] ^ xs[1] ^ xs[2]
    y4 = ys[0] ^ ys[1] ^ ys[2]
    
    return x4, y4

# 학점계산 
def convert_grade_to_gpa(grade):
    """문자열 학점을 평점(GPA)으로 변환합니다."""
    grade_map = {
        'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    return grade_map.get(grade, "유효하지 않은 학점")

# 그릇 
def calculate_dish_height(shapes):
    """그릇의 모양에 따라 높이를 계산합니다. (첫 그릇 10, 같은 방향 +5, 다른 방향 +10)"""
    if not shapes:
        return 0
        
    height = 10
    for i in range(1, len(shapes)): 
        if shapes[i] == shapes[i-1]:
            height += 5
        else:
            height += 10
    return height

# TGN 
def recommend_ad(r, e, c):
    """광고 수익(e), 비용(c)을 광고 안 했을 때 수익(r)과 비교하여 추천합니다."""
    ad_profit = e - c
    
    if ad_profit > r:
        return "advertise"
    elif ad_profit < r:
        return "do not advertise"
    else:
        return "does not matter"

# 0 = not cute / 1 = cute (10886)
def determine_cute(votes):
    """0(not cute)과 1(cute) 투표 중 다수 의견을 판별합니다."""
    one_count = votes.count(1)
    zero_count = votes.count(0)
    
    if one_count > zero_count:
        return "Junhee is cute!"
    else:
        return "Junhee is not cute!" 

# 삼근이의 친구들 
def count_friend_pairs(n_students, pairs):
    """학생 수와 친구 관계 쌍을 받아 관계 수를 반환합니다."""
    return len(pairs)

# Baseball 
def analyze_baseball_score(y_scores, k_scores):
    """연세(Y)와 고려(K)의 점수를 비교하여 승자를 판정합니다."""
    y_total = sum(y_scores)
    k_total = sum(k_scores)
    
    if y_total > k_total:
        return "Yonsei"
    elif k_total > y_total:
        return "Korea"
    else:
        return "Draw"

# Yangjaong Of The Year
def find_top_drinker(country_data):
    """술 소비량이 가장 많은 나라를 찾습니다."""
    if not country_data:
        return "데이터 없음"
    
    return max(country_data, key=country_data.get)

# 테스트 코드 (실행 환경에서 함수의 작동을 확인하는 데 사용)

if __name__ == "__main__":
    print(f"주사위 세계 (4개): {dice_world_outcomes(4)}")
    print(f"OX퀴즈 ('OOXO') 점수: {calculate_ox_quiz_score('OOXO')}")

    print(f"알람 시계 (0, 30) 45분 전: {set_alarm_early(0, 30)}")
    print(f"사분면 (-2, -5): {check_quadrant(-2, -5)}")
    
    print(f"학점계산 (B+): {convert_grade_to_gpa('B+')}")
    consumption = {'KOR': 100, 'JPN': 120, 'USA': 80}
    print(f"Top Drinker: {find_top_drinker(consumption)}")
