# 문제 설명
# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
# 예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

# b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
# n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
# a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
# 따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

# 문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.

# 제한사항
# 1 ≤ s의 길이 ≤ 10,000
# s은 영어 소문자로만 이루어져 있습니다.

# 입출력 예
# s     	result
# "banana"	[-1, -1, -1, 2, 2, 2]
# "foobar"	[-1, -1, 1, -1, -1, -1]


s = "banana"
# 1. 내가 작성한 코드
def solution(s):
    result = []
    tmp = ""

    for i in range(len(s)):
        if s[i] in tmp: # tmp에 이미 있으면 거리를 result에 추가
            result.append((len(tmp)) - tmp.rindex(s[i]))
        else:
            result.append(-1)
        tmp += s[i]

    return result
print(solution(s))

# dictionary 를 사용하면
# {} 중괄호가 크게 만들어진다.
# 이 중괄호에 데이터를 넣는데 방법은 dict[키[값]] = 값 형태로 넣을 수 있음

# 2. 최적 코드
def good_solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            print(f"i: {i}")
            print(f"dic[s[i]]: {dic[s[i]]}")
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
        print(dic)

    return answer
print(good_solution(s))