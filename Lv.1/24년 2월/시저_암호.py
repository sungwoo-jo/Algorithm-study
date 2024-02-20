# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

# 입출력 예
# s	        n	result
# "AB"	    1	"BC"
# "z"	    1	"a"
# "a B z"	4	"e F d"

s = "a B z"
n = 4

# 1. 내가 작성한 코드
def solution(s, n):
    big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    little = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = ""
    for i in s:
        if i == " ": # 공백이면 공백 더해주기
            result += " "
        else:
            if ord("A") <= ord(i) <= ord("Z"): # 대문자일때
                result += big[(ord(i)+n-65) % 26] # i를 아스키로 변환한 값에 n을 더해주고 A 글자만큼 뺀 값에 26을 나눴을 때의 나머지
            elif ord("a") <= ord(i) <= ord("z"): # 소문자일때
                result += little[(ord(i)+n-97) % 26] # i를 아스키로 변환한 값에 n을 더해주고 a 글자만큼 뺀 값에 26을 나눴을 때의 나머지
    return result

print(solution(s,n))

# 2. 최적 코드
def good_solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

print(good_solution(s, n))

