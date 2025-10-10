# 1. 선택 정렬 (Selection Sort)
data_sel = [5, 3, 8, 4, 9, 1, 6, 2, 7]
def selection_sort(A):
    n = len(A)
    # 외부 루프: n-1번 반복
    for i in range(n - 1):
        least = i # 최소 항목의 인덱스를 현재 위치 i로 초기화
        # 내부 루프
        for j in range(i + 1, n):
            # 비교 연산
            if (A[j] < A[least]):
                least = j # 최소 항목 인덱스 갱신
        # 튜플 교환
        A[i], A[least] = A[least], A[i]
    return A
print(f"1. 선택 정렬 전: {data_sel}")
selection_sort(data_sel)
print(f"   선택 정렬 후: {data_sel}")
