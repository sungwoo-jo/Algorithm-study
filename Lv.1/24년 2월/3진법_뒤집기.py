# 1. 내가 작성한 코드
# (내일 divmod 밖에 방법 없는지 보기)
n = 45

def solution(n):
    answer = ''
    result = 0

    mok = n
    while mok > 0:
        answer += str(mok % 3)
        mok //= 3

    print(answer)

    answer = answer[::-1]

    cnt = 1

    for i in range(len(answer)):
        print(int(answer[i]) * i * cnt)
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

    for i in arr: # 다시 삼진법으로 계산
        answer += int(i) * cnt
        cnt *= 3

    return answer

print(good_solution(125))