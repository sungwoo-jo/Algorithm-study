# 문제 설명
# 숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

# 예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다.
# 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

# 제한사항
# 1 ≤ p의 길이 ≤ 18
# p의 길이 ≤ t의 길이 ≤ 10,000
# t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.

# 3141592 일 때
# 314 141 415 159 592

t = "1"
p = "1"

# 1. 내가 작성한 코드
def solution(t, p):
    i = 0
    j = len(p)
    arr = []
    while j <= len(t):
        if int(t[i:j]) <= int(p):
            arr.append(t[i:j])
        i += 1
        j += 1
    return len(arr)

print(solution(t, p))

# 2. 최적 코드
def good_solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

print(good_solution(t, p))