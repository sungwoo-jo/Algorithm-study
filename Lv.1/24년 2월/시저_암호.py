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

# 문제 해결 생각
# 1. 아스키코드로 구함
# 2. result에 append
#   2-1 if s[i]가 공백이면 공백을 append
#   2-2 else s[i]가 알파벳이므로 +1한 값을 append
# 3. return result

s = "a B z"
n = 4

def solution(s,n):
    result = ""
    # little = []
    # big = []
    #
    # for i in range(65, 91): # 대문자 배열 생성
    #     little.append(chr(i))
    # for i in range(97, 123): # 소문자 배열 생성
    #     big.append(chr(i))

    for i in s:
        if i == " ": # 공백이면 공백 더해주기
            result += " "
        else:
            if ord(i) + n <= 65 <= 90:
                if ord(i) + n > 90:
                    # print(chr(ord(i) + n - 26))
                    result += chr(ord(i) + n - 26)
                else:
                    # print(chr(ord(i) + n))
                    result += chr(ord(i) + n)
            else:
                if ord(i) + n > 122:
                    # print(chr(ord(i) + n - 26))
                    result += chr(ord(i) + n - 26)
                else:
                    # print(chr(ord(i) + n))
                    result += chr(ord(i) + n)

    return result



print(solution(s,n))