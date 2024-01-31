def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer

if __name__ == "__main__":
    arr = [2, 36, 1, 3]
    divisor = 1

    print(solution(arr, divisor))