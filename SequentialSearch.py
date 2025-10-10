# 2. 순차 탐색
def sequential_search(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i  # 목표값을 찾으면 인덱스 반환
    return -1  # 목표값이 없으면 -1 반환
list_seq = [10, 20, 30, 40, 50]
target_val = 30
print(f"2. 순차 탐색 리스트: {list_seq}, 목표값: {target_val}")
print(f"   결과 (인덱스): {sequential_search(list_seq, target_val)}")
