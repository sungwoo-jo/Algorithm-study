# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

# 짝수면 (s / 2) - 1 번째부터 2개 출력, 홀수면 (s / 2) - 1 번째부터 1개 출력

def solution(s):
    # answer = ''
    length = int(len(s)/2)

    if len(s) % 2 == 0: # 짝수일때
        return s[length-1:length+1]
    else: # 홀수일때
        return s[length-1+1]

    # return answer

s = "qwer"

print(solution(s))