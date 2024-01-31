# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

# 1. 내가 작성한 코드
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

answer = []
def my_solution(arr1, arr2):
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j]) # 동일한 행렬의 더한 값을 리스트로 만듬
        answer.append(arr_sum) # 끝난 행은 number에 추가
    return answer

print(my_solution(arr1, arr2))

# 2. 최적 코드
def good_solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

print(good_solution(arr1, arr2))