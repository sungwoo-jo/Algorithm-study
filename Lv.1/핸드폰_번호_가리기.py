# 문제 설명
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.

phone_number = "027778888"

# 1. 내가 작성한 코드
def my_solution(phone_number):
    return phone_number.replace(phone_number[0:-4], (len(phone_number) - 4) * "*")

print(my_solution(phone_number))

# 2. 최적 코드
def good_solution(phone_number):

    return "*"*(len(phone_number)-4)+phone_number[-4:]

print(good_solution(phone_number))