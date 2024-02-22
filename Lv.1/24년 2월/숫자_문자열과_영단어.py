# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	    zero
# 1	    one
# 2	    two
# 3	    three
# 4	    four
# 5	    five
# 6	    six
# 7	    seven
# 8	    eight
# 9	    nine

# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 입출력 예
#       s	            result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	123


s = "one4seveneight"

# 1. 내가 작성한 코드
def solution(s):
    result = ""
    dictionary = dict({
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    })

    for i in range(len(s)):
        if s[i].isnumeric():
            result += str(s[i])
            continue
        else:
            for j in range(i + 1, len(s)): # 문자인경우
                if s[i:j+1] in dictionary:
                    result += str(dictionary[s[i:j+1]])
    return int(result)
print(solution(s))


# 2. 최적 코드
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def good_solution(s):
    answer = s
    for key, value in num_dic.items(): # num_dic을 key, value로 전달받음
        answer = answer.replace(key, value) # 전달받은 key를 기준으로 value 값으로 치환함 ex) one4seveneight -> 1478
    return int(answer)

print(good_solution(s))