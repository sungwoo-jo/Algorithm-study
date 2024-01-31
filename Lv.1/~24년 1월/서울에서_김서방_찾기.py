def solution(seoul):
    answer = seoul.index("Kim")

    return "김서방은 " + str(answer) + "에 있다"

if __name__ == "__main__":
    seoul = ["Jane", "Kim"]

    print(solution(seoul))
