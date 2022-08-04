def solution(arr):
    answer = []

    # 먼저 첫번째 숫자를 넣어놓고 그 후로 배열 안의 숫자가 스택의 마지막 원소와 같으면 넣지 않고 다르면 놓는다
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])

    return answer