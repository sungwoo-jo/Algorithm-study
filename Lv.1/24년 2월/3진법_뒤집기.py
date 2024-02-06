# 1. 내가 작성한 코드
# (내일 divmod 밖에 방법 없는지 보기)
n = 45
answer = []
namuji = 1

mok = n
while mok > 0:
    mok //= 3

    # print("mok:", mok)
    namuji = mok % 3
    # print("namuji:", namuji)
    answer.append(namuji)

print(answer)

# 2. 최적 코드
