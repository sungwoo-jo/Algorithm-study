# 1. 내가 작성한 코드
arr = [1,3,3,0,1]

def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer

print(solution(arr))

# 2. 최적 코드
def good_solution(s):
    result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result