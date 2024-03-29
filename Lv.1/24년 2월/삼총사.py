# 문제 설명
# 한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

# 한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# 3 ≤ number의 길이 ≤ 13
# -1,000 ≤ number의 각 원소 ≤ 1,000
# 서로 다른 학생의 정수 번호가 같을 수 있습니다.

# 입출력 예
# number	result
# [-2, 3, 0, 2, -5]	2
# [-3, -2, -1, 0, 1, 2, 3]	5
# [-1, 1, -1, 1]	0

number = [-3, -2, -1, 0, 1, 2, 3]

# 1. 내가 작성한 코드
def solution(number):
    cnt = 0
    for ie in range(0, len(number) - 2):
        for je in range(ie+1, len(number) - 1):
            for ke in range(je+1, len(number)):
                if number[ie] + number[je] + number[ke] == 0:
                    cnt += 1
    return cnt

# 2. 최적 코드
def good_solution(number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3):
        if sum(i) == 0 :
            cnt += 1
    return cnt

print(solution(number))
print(good_solution(number))

arr = [1,2,3,4,5,6,7,8]

from itertools import combinations
for i in combinations(number,3):
    print(i)