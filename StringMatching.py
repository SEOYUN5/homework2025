# 3. 문자열 매칭 (String Matching)
def string_matching(T, P):
    """억지 기법 문자열 매칭 알고리즘 (T: 텍스트, P: 패턴)"""
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        j = 0
        while j < m and P[j] == T[i + j]:
            j = j + 1

        if j == m:
            return i

    return -1
text_T = "HELLO WORLD"
pattern_LO = "LO"
pattern_HI = "HI"

result_LO = string_matching(text_T, pattern_LO)
print(f"3. 문자열 매칭:\n{pattern_LO} in {text_T} → {result_LO} (매칭 성공)")

result_HI = string_matching(text_T, pattern_HI)
print(f"{pattern_HI} in {text_T} → {result_HI} (패턴이 텍스트에 없음)")
print("-" * 40)
