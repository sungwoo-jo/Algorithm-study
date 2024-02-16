# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 입출력 예
# n	result
# 45	7
# 125	229

# 1. 내가 작성한 코드
n = 125

def solution(n):
    answer = ""
    result = 0

    while n > 0:
        m = n % 3
        n = n // 3
        answer += str(m)

    answer = answer[::-1]

    cnt = 1
    for i in answer:
        result += int(i) * cnt
        cnt *= 3

    return result

print(solution(n))

# 2. 참고 코드
def good_solution(n):
    answer = 0
    arr = '' # 삼진법을 임시 저장할 문자열

    while n > 0: # 삼진법 계산
        arr += str(n % 3)
        n //= 3

    arr = arr[::-1] # 문자열을 반대로 정렬
    cnt = 1

    for i in arr: # 다시 십진법으로 계산
        answer += int(i) * cnt
        cnt *= 3
        # print("i:",i)
        # print("cnt:", cnt)

    return answer

print(good_solution(n))